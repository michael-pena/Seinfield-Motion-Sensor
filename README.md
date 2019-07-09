# Seinfeld Motion Sensor


<h3>What is this project?</h3>
This is a dumb project written in python that's made on the Raspberry Pi 3B+. It plays a random Seinfeld bass riff when you set off a pir motion sensor. Put it next to a doorway for anyone who enters for a maximum 90's sitcom effect. <br> <br>

A demonstration can be found <a href="https://drive.google.com/file/d/1UFcWh7oA0bk83CSIYuuevMXwviXVxReI/view?usp=sharing"> here. </a> <br>

<h3>Library Dependencies</h3>

<code>sudo pip install gpiozero </code> <br>
<code>sudo apt-get install python-pygame </code> <br>


<h3>What You Will Need</h3>
1. Raspberry Pi 3 <br>
2. <a href=https://www.microcenter.com/product/476340/velleman-pir-motion-sensor-for-arduino>PIR Motion Sensor </a> <br>
3. Female to Female jumper Wires <br>
4. Powered Computer Speakers (I used some cheap logitech ones like <a href=https://www.amazon.com/Logitech-S120-2-0-Stereo-Speakers/dp/B000R9AAJA/ref=sr_1_10?keywords=logitech+speakers&qid=1562628803&s=gateway&sr=8-10>these.</a>) <br>

<h3>Directions</h3>
I'm going to assume you're a beginner and go through the basics of setting up this project. When starting out with any Raspberry Pi project it's always a good idea to familiarize yourself with a GPIO diagram like this one. <br>

![alt tag](https://github.com/michael-pena/Seinfield-Motion-Sensor/blob/master/rp2_pinout.png)


1. the first step is to connect the jumper wires on the motion sensor to the board. Using three jumper wires connect the PIR motion sensor in the following manner using the above diagram, on the sensor connect: VCC to a 5V Power Pin (Pins 2 or 4), OUT to GPIO 4 (Pin 7), and GND to GND (Pin 6).

2. Now assuming you have Raspbian installed, plug in the speakers into Raspberry Pi's audio out jack and power on the Pi.

3. Make sure you have Python and Pip installed and download all the Dependencies listed above.

4. git clone this repo into your home directory.

5. run the program with <code>python seinfeld.py</code>
