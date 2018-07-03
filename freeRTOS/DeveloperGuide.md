# About the FreeRTOS Kernel
The FreeRTOS kernel is an open source software maintained by Amazon.  

The FreeRTOS kernel is ideally suited to deeply embedded real-time applications that use microcontrollers or small microprocessors. This type of application normally includes a mix of both hard and soft real-time requirements.  

Soft real-time requirements are those that state a time deadline, but breaching the deadline does not render the system useless. For example, responding to keystrokes too slowly might make a system seem annoyingly unresponsive without actually making it unusable.  

Hard real-time requirements are those that state a time deadline and breaching the deadline does result in absolute failure of the system. For example, a driver's airbag has the potential to do more harm than good if it responded to crash sensor inputs too slowly.  

The FreeRTOS kernel is a real-time kernel (or real-time scheduler) on top of which embedded applications can be built to meet hard real-time requirements. It allows applications to be organized as a collection of independent threads of execution. On a processor that has only one core, only a single thread can be executing at any one time. The kernel decides which thread should be executing by examining the priority assigned to each thread by the application designer. In the simplest case, the application designer could assign higher priorities to threads that implement hard real-time requirements, and lower priorities to threads that implement soft real-time requirements. This would ensure that hard real-time threads are always executed ahead of soft real-time threads, but priority assignment decisions are not always that simplistic.  

Don't be concerned if you don't fully understand the concepts in the previous paragraph yet. The guide covers them in detail and provides many examples to help you understand how to use a real-time kernel and the FreeRTOS kernel in particular.  

## Value Proposition
The unprecedented global success of the FreeRTOS kernel comes from its compelling value proposition. The FreeRTOS kernel is professionally developed, strictly quality-controlled, robust, supported, does not contain any intellectual property ownership ambiguity, and is truly free to use in commercial applications without any requirement to expose your proprietary source code. You can take a product to market using the FreeRTOS kernel without paying any fees, and thousands of people do just that. If, at any time, you would like to receive additional backup, or if your legal team require additional written guarantees or indemnification, then there is a simple low cost commercial upgrade path. Peace of mind comes with the knowledge that you can opt to take the commercial route at any time you choose.

## A Note About Terminology
In the FreeRTOS kernel, each thread of execution is called a task. Although there is no consensus on terminology in the embedded community, thread can have a more specific meaning in some fields of application.

## Why Use a Real-time Kernel?
There are many well established techniques for writing good embedded software without the use of a kernel, and, if the system being developed is simple, then these techniques might provide the most appropriate solution. In more complex cases, using a kernel is preferable, but where the crossover point occurs is always subjective.  

Task prioritization can help ensure an application meets its processing deadlines, but a kernel can bring other less obvious benefits, too:  

- Abstracting away timing information

The kernel is responsible for execution timing and provides a time-related API to the application. This allows the structure of the application code to be simpler and the overall code size to be smaller.

- Maintainability/extensibility

Abstracting away timing details results in fewer interdependencies between modules and allows the software to evolve in a controlled and predictable way. Also, the kernel is responsible for timing, so application performance is less susceptible to changes in the underlying hardware.

- Modularity

Tasks are independent modules, each of which should have a well-defined purpose.

- Team development

Tasks should also have well-defined interfaces, allowing easier development by teams.

- Easier testing

If tasks are well-defined independent modules with clean interfaces, they can be tested in isolation.

- Code reuse

Greater modularity and fewer interdependencies result in code that can be reused with less effort.

- Improved efficiency

Using a kernel allows software to be completely event-driven, so no processing time is wasted by polling for events that have not occurred. Code executes only when there is something that must be done.

Counter to the efficiency saving is the need to process the RTOS tick interrupt and to switch execution from one task to another. However, applications that don't make use of an RTOS normally include some form of tick interrupt anyway.

- Idle time

The Idle task is created automatically when the scheduler is started. It executes whenever there are no application tasks wishing to execute. The idle task can be used to measure spare processing capacity, to perform background checks, or simply to place the processor into a low-power mode.

- Power management

The efficiency gains by using an RTOS allow the processor to spend more time in a low power mode.

Power consumption can be decreased significantly by placing the processor into a low power state each time the Idle task runs. The FreeRTOS kernel also has a tickless mode that allows the processor to enter and remain in the low power mode for longer.

- Flexible interrupt handling

Interrupt handlers can be kept very short by deferring processing to either a task created by the application writer or the FreeRTOS daemon task.

- Mixed processing requirements

Simple design patterns can achieve a mix of periodic, continuous, and event-driven processing within an application. In addition, hard and soft real-time requirements can be met by selecting appropriate task and interrupt priorities.

## FreeRTOS Kernel Features
The FreeRTOS kernel has the following standard features:

- Preemptive or cooperative operation
- Very flexible task priority assignment
- Flexible, fast, and lightweight task notification mechanism
- Queues
- Binary semaphores
- Counting semaphores
- Mutexes
- Recursive mutexes
- Software timers
- Event groups
- Tick hook functions
- Idle hook functions
- Stack overflow checking
- Trace recording
- Task runtime statistics gathering
- Optional commercial licensing and support
- Full interrupt nesting model (for some architectures)
- A tickless capability for extreme low power applications
- Software-managed interrupt stack when appropriate (this can help save RAM)  

# FreeRTOS Kernel Distribution
The FreeRTOS kernel is distributed as a single zip file archive that contains all the official FreeRTOS kernel ports and a large number of preconfigured demo applications.  

## Understanding the FreeRTOS Kernel Distribution
The FreeRTOS kernel can be built with approximately 20 different compilers, and can run on more than 30 different processor architectures. Each supported combination of compiler and processor is considered to be a separate FreeRTOS port.

## Building the FreeRTOS Kernel
You can think of FreeRTOS as a library that provides multitasking capabilities to what would otherwise be a bare metal application.  

FreeRTOS is supplied as a set of C source files. Some of the source files are common to all ports, while others are specific to a port. Build the source files as part of your project to make the FreeRTOS API available to your application. To make this easy for you, each official FreeRTOS port is provided with a demo application. The demo application is preconfigured to build the correct source files and include the correct header files.  

Demo applications should build out of the box. However, a change made in the build tools since the demo was released can cause issues. For more information, see Demo Applications later in this topic.  

## FreeRTOSConfig.h
FreeRTOS is configured by a header file called FreeRTOSConfig.h.  

FreeRTOSConfig.h is used to tailor FreeRTOS for use in a specific application. For example, FreeRTOSConfig.h contains constants such as configUSEPREEMPTION, the setting of which defines whether the cooperative or preemptive scheduling algorithm will be used. FreeRTOSConfig.h contains application-specific definitions, so it should be located in a directory that is part of the application being built, not in a directory that contains the FreeRTOS source code.  

A demo application is provided for every FreeRTOS port, and every demo application contains a FreeRTOSConfig.h file. Therefore, you never need to create a FreeRTOSConfig.h file from scratch. Instead, we recommend that you start with and then adapt the FreeRTOSConfig.h used by the demo application provided for the FreeRTOS port in use.  

## The Official FreeRTOS Kernel Distribution
FreeRTOS is distributed in a single zip file. The zip file contains source code for all the FreeRTOS ports and project files for all the FreeRTOS demo applications. It also contains a selection of FreeRTOS+ ecosystem components and a selection of FreeRTOS+ ecosystem demo applications.  

Don't worry about the number of files in the FreeRTOS distribution. Only a small number of files are required in any one application.  



# Heap Memory Management
# Task Management
# Queue Management
# Software Timer Management
# Interrupt Management
# Resource Management
# Event Groups
# Task Notifications
# Developer Support
# Troubleshooting
