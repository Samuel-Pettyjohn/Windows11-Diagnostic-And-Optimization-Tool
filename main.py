import sys

if __name__ == '__main__':
    # Launch GUI if no CLI args, else fallback to CLI
    if len(sys.argv) > 1:
        import modules.cli as cli
        cli.run()
    else:
        from ui.gui import gui_main
        gui_main()