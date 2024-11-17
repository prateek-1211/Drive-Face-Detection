Packages to Install:
To run the above code, ensure you have the following Python packages installed:

OpenCV (for video processing and webcam access):

bash:pip install opencv-python
     MediaPipe (for facial landmarks detection):

bash:pip install mediapipe
     SciPy (for calculating Eye Aspect Ratio using Euclidean distance):

bash:pip install scipy
     Pygame (for playing alert sounds):

bash:pip install pygame

# Distraction Detection System  

## **Overview**  
The *Distraction Detection System* is a real-time solution designed to detect driver distractions, such as drowsiness, using computer vision techniques. By analyzing eye movements and calculating the Eye Aspect Ratio (EAR), the system identifies signs of inattention and plays an alert sound to regain the driver's focus.  

## **Features**  
- **Real-Time Monitoring**: Tracks eye landmarks using a webcam.  
- **Alert System**: Triggers a warning sound when signs of drowsiness are detected.  
- **Visual Feedback**: Displays tracked eye points on the screen for better understanding.  

## **Technologies Used**  
- **Python**: Core programming language.  
- **OpenCV**: For video capture and image processing.  
- **MediaPipe**: For face and eye landmark detection.  
- **SciPy**: For mathematical calculations of Eye Aspect Ratio (EAR).  
- **Pygame**: For audio playback of alert sounds.  

## **Installation**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/distraction-detection-system.git
