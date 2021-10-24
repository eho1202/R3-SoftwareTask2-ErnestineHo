# R3-SoftwareTask2-ErnestineHo  
Software Training Package #2

In this project we are to write an two python files. First an input client file for receiving the keyboard/controller output and sends it to the client. Second an output server file for receiving data over TCP and printing the output.    

Keyboard controls are used in this project. The inputs are:
- 0, 1, 2, 3, 4, 5 for speed controls
- w, a, s, d for direction controls
- esc to disconnect

Once client is connected to the server, any keystrokes from the client side will be sent to the server for output.
Depending on the input, the output would display the change in speed or the direction the rover is going.  
If any number between 0 and 5 is pressed, the output would be for example: "Speed set to 5"
If wasd is pressed, the output would be for example: "[f255][f255][f255][f255]"
If the esc key is pressed, the client will disconnect but server will stay on.

# Demo Video
https://user-images.githubusercontent.com/42323715/138600253-25412092-7fe9-4aea-b030-efbbf750d5b6.mp4

