# TicTacToe

**Overview**
A Tic Tac Toe program that allows for in-person play on the terminal, with plans to implement AI opponents and a GUI with the Turtle library.

**Project Nature**
This project relies heavily on handling user input effectively, structuring logical branches effectively, and understanding possible points of intersection between object-oriented and functional programming.

This project in particular marks what is essentially my first effort at coming up with a sizeable program from scratch. Thus, there have been several issues with the organization, scoping, implementation, etc. of this project. The point is not necessarily to fix all of these: it is instead to learn from them so that future projects are done better.

So far, I've learned much about several things I've attempted to put into this project, including:
- How to structure larger projects
- How to think long-term on greenfield projects
- Handling user input
- Implementing automated tests
and more!

**Implementation Decisions**
- Importing os allows for some QOL implmentation across different operating systems. The project actually has yet to be tested on different OSs though.
- Making the X and O pieces on the board objects actually seems like a pretty bad software engineering practice, but it opens up possible implementation additions for future work as well as being a combination of functional and object-oriented programming in itself.
- Using try / except statements for handling user inputs allows for the redundant behavior of do-while loops while also allowing for further checks on data type, formatting specifics, etc. and seems to be a clean solution.
- The iterative solution for win checking is currently broken. Implementing a recursive solution would be much cleaner and more widely applicable, but developing one has proven challenging and is not yet complete.

