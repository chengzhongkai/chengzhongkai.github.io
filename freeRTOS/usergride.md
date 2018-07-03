# What Is Amazon FreeRTOS?
Amazon FreeRTOS consists of the following components:
- A microcontroller operating system based on the FreeRTOS kernel
- Amazon FreeRTOS libraries for connectivity, security, and over-the-air (OTA) updates.
- A configuration wizard that allows you to download a zip file that contains everything you need to get started with Amazon FreeRTOS.
- Over-the-air (OTA) Updates.
- The Amazon FreeRTOS Qualification Program.
## The FreeRTOS Kernel
The FreeRTOS kernel is a real-time operating system kernel that supports numerous architectures and is ideal for building embedded microcontroller applications. The kernel provides:
- A multitasking scheduler.
- Multiple memory allocation options (including the ability to create statically allocated systems).
- Inter-task coordination primitives, including task notifications, message queues, multiple types of semaphores, and stream and message buffers.
## Amazon FreeRTOS Libraries
Amazon FreeRTOS includes libraries that enable you to:
- Securely connect devices to the AWS IoT cloud using MQTT and device shadows.
- Discover and connect to AWS Greengrass cores.
- Manage Wi-Fi connections.
## Amazon FreeRTOS Configuration Wizard
The Amazon FreeRTOS configuration wizard enables you to configure and download a package that contains everything you need to write an application for your microcontroller-based devices:
- The FreeRTOS kernel
- Amazon FreeRTOS libraries
- Platform support libraries
- Hardware drivers  

You can download a package with a predefined configuration or create your own configuration by selecting your hardware platform and the libraries required for your application. These configurations are saved in AWS and are available for download at any time.  
The Amazon FreeRTOS configuration wizard is part of the AWS IoT console. You can find it by choosing the link above or by browsing to the AWS IoT console.  
__To open the Amazon FreeRTOS configuration wizard__  
1. Browse to the AWS IoT console.
2. From the navigation pane choose __Software__.
3. Under __Amazon FreeRTOS Device Software__ choose __Configure Download__.

## Over-the-Air Updates (Beta)
Internet-connected devices can be in use for a long time, and must be updated periodically to fix bugs and improve functionality. Often these devices must be updated in the field and need to be updated remotely or "over-the-air". The Amazon FreeRTOS Over-the-Air (OTA) Update service enables you to:
- Digitially sign firmware prior to deployment.
- Securely deploy new firmware images to a single device, a group of devices, or your entire fleet.
- Deploy firmware to devices as they are added to groups, reset, or reprovisioned.
- Once deployed to devices, verify the authenticity and integrity of the new firmware.
- Monitor the progress of a deployment.
- Debug a failed deployment.

For more information about OTA updates, see:
- Amazon FreeRTOS Over-the-Air Updates
- OTA Demo Application

## Amazon FreeRTOS Qualification Program
The Amazon FreeRTOS Qualification Program (Amazon FQP) is for microcontroller vendors who want to qualify their microcontroller-based hardware on Amazon FreeRTOS. The goal of Amazon FQP is to ensure that developers can use Amazon FreeRTOS on their choice of microcontroller-based hardware. In order to deliver a consistent experience for developers, the Amazon FQP outlines a set of security, functionality, and performance requirements that all microcontrollers (and the associated hardware abstraction layers and drivers) must meet.

# Getting Started with Amazon FreeRTOS
# Amazon FreeRTOS Developer Guide
# Amazon FreeRTOS Demo Projects
# Amazon FreeRTOS Porting Guide
