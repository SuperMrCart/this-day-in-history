import ctypes
import keyboard  # Install this library with `pip install keyboard`

# Constants for Windows API
SW_HIDE = 0
SW_SHOW = 5

# Define callback function for EnumWindows
WNDENUMPROC = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)

def get_taskbar_handles():
    """Retrieve handles for all taskbars (including multi-monitor setups)."""
    handles = []

    def enum_windows_callback(hwnd, lParam):
        """Callback function to check each window's class name."""
        class_name = ctypes.create_unicode_buffer(256)
        ctypes.windll.user32.GetClassNameW(hwnd, class_name, 256)

        # Check for primary and secondary taskbars
        if class_name.value in ["Shell_TrayWnd", "Shell_SecondaryTrayWnd"]:
            handles.append(hwnd)
        return True

    # Enumerate all top-level windows
    ctypes.windll.user32.EnumWindows(WNDENUMPROC(enum_windows_callback), 0)

    return handles

def hide_taskbars():
    """Hide all Windows taskbars."""
    handles = get_taskbar_handles()
    if not handles:
        print("No taskbars found.")
        return

    for handle in handles:
        ctypes.windll.user32.ShowWindow(handle, SW_HIDE)
    print("All taskbars hidden.")

def show_taskbars():
    """Show all Windows taskbars."""
    handles = get_taskbar_handles()
    if not handles:
        print("No taskbars found.")
        return

    for handle in handles:
        ctypes.windll.user32.ShowWindow(handle, SW_SHOW)
    print("All taskbars shown.")

def toggle_taskbars():
    """Toggle the visibility of all Windows taskbars."""
    handles = get_taskbar_handles()
    if not handles:
        print("No taskbars found.")
        return

    # Check if the first taskbar is visible (assume all are in the same state)
    is_visible = ctypes.windll.user32.IsWindowVisible(handles[0])
    if is_visible:
        hide_taskbars()
    else:
        show_taskbars()

if __name__ == "__main__":
    print("Press 'Ctrl+Alt+H' to toggle the taskbar visibility on all monitors.")
    print("Press 'Ctrl+Alt+Q' to quit the program.")

    # Set up hotkeys
    keyboard.add_hotkey("ctrl+alt+h", toggle_taskbars)  # Toggle taskbar visibility
    keyboard.wait("ctrl+alt+q")  # Exit the program when 'Ctrl+Alt+Q' is pressed
    print("Program exited.")