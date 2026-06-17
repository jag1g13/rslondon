---
layout: single
title: "RSLondonSouthEast 2020: Abstracts"
permalink: /rslondonse-2020/abstracts/
---

[< Back to RSLondonSouthEast 2020: Schedule](/rslondon/rslondonse-2020/agenda)

### **Talk Abstracts**

#### **Full Talks**

  
  
  

**Challenges of Managing Research Compute Platforms at The Turing**

**Tomas Lazauskas**, The Alan Turing Institute

Almost every research organisation owns or has access to on-perm or cloud research compute platforms for their computationally and data intensive research. For most organisations it is a mixture of both, which makes the task of ensuring that all the platforms are efficiently exploited even more challenging.

At The Alan Turing Institute we currently provide access to six on-perm and one cloud platform, and we expect these numbers to increase as the Institute continues to grow. With the increasing number of researchers and research compute platforms, the research (software/data science) engineering group at the Turing has faced various challenges ranging from establishing processes for our researchers to make requests and allocations for compute resources, to managing cloud compute budgets and coordinating resource allocation panels.

In my presentation I would like to share our group’s experience of facing these challenges, tools that we have developed to support our researchers (such as webapps) and my personal experience of leading a small team managing compute platforms at The Turing.

  
  
  

**Inclusivity in tech? The label “women in tech” and its effect on the RSE community**

**Mariann Hardey**, University of Durham  
Joanna Leng, University of Leeds

The promotion of diversity, inclusivity and equality are potent themes in the tech sector and around the popular narratives about inclusivity in tech.

The label ‘women in tech’ (WiT) is distinct in this narrative, but little attention has been given to the potential for bias and the consequences of the label directly within the RSE community. In particular, how this narrative impacts on careers, training and implementation of diversity policies within institutions, commercial companies utilising RSE workers, or in the ‘gig’ economy.

Bias is implicit with the application of any label and the popularity of the alignment of terms ‘women’ with ‘tech’ warrants attention and clarification.

The WiT label has a heritage in popular press articles demonstrating a ‘problem’ about the lack of women in tech jobs. In parallel the label has also become a vehicle to amplify divisions in the wider tech sector. These inconsistencies fail to reflect the standards of work and career structure in RSE.

Our focus on “bias” is consistent with the impact of technology on the labour process, categories for evaluating skills and inclusion of new policies to remedy gender-bias.

We are concerned primarily with what is usually made implicit in the adoption of the WiT label and iteration as common terminology to remedy a lack of diversity in RSE.

Attention is given to the formalisation of the label WiT and expected outcomes as critical to understanding ways that the RSE community can implement, and support diversity through models of work and skills training.

  
  
  

**Continuous Integration for Research Software**

**Christopher Cave-Ayland**, Imperial College London

The practice of continuous integration (CI) has become a cornerstone of modern software engineering, providing widely accepted advantages in development speed and quality through improved feedback at all stages of a project. A proliferation of platforms offering CI services has provided a competitive environment with an overwhelming amount of choice. There remains however a unique set of challenges around incorporating CI in research software development in an academic environment.

Research software often provides a portfolio of requirements that differ significantly from those of typical commercial and open source projects, including complex dependencies (that can include other pieces of research software), support for accelerators, multi-node scaling, and specialist compilers and operating systems. In addition to technical requirements, there is a cultural lag in the adoption of software development practices in academia and often a lack of appreciation of what they can provide.

This talk will discuss some of the experiences the Research Software Engineering team at Imperial College has had with CI in the context of academic software development and what steps research institutions can take to support and promote uptake. We will highlight a case study, provided by the code Nektar++, that illustrates how a subset of these considerations interact with current CI service offerings and self-hosted solutions.

  
  
  

**SciGateway & DataGateway: the portals to facilities science and facilities data**

**Alejandra Gonzalez-Beltran**, Louise Davies, Goel Biju, Emily Lewis, Stuart Pullinger, Catherine Jones  
Scientific Computing Department, Science and Technology Facilities Council

Large scale facilities, such as synchrotrons, neutron and muon sources, lasers and accelerators, generate vast amounts of data that need to be managed in an efficient way, supporting data ingestion for long-term storage and archival, as well as data analysis and data publication workflows.

In this talk, we will present our work developing SciGateway and DataGateway, which are open source components. SciGateway is a ReactJs-based parent application within a micro-front end architecture. It provides features such as authentication and authorisation functionality, notifications, and cookies management common to other applications that are access points to data and/or compute resources.

DataGateway is another ReactJs-based component in the architecture, focusing on providing data discovery and data access functionality to the data. The data is organised according to the data hierarchy that reflects the data pipelines in each facility. The data is shown in a tabular format depicting the main metadata fields.

We will discuss the software architecture as well as the agile software development process and best practices being used.

  
  
  

**Designing and building ‘Colouring London’ to collect and visualise open building data**

**Tom Russell**, University of Oxford

“Colouring London” is a web application and knowledge exchange platform collecting information on every building in London, aiming to involve volunteers of all ages and abilities, from built environment specialists to schoolchildren. Data collected is made openly available under the ODbL, and the core web application code is open under the GPL.

This talk will introduce the motivation for Colouring London – why do we need or want to collect data about individual buildings? What data can and should we collect? – and will discuss the design and implementation challenges and approaches taken in making an openly editable, ethically considerate, data collection and visualisation platform which covers the roughly 3 million buildings in Greater London.

<https://colouring.london/>

  
  
  

**A trip to the operating room: combined imaging for guiding brain surgery**

**Anastasis Georgoulas**, Roland Guichard, David Pérez-Suárez  
University College London

Surgery for removing brain tumours relies heavily on analysing images from a variety of sources, such as magnetic resonance, ultrasound and tomography. Some of these are acquired in real time, while others are the result of preprocessing, and provide complementary information. In a common setup, images are displayed on different screens of specialised hardware. This limits staff’s ability to draw on multiple sources at once, and locks them into vendor-specific tools for interacting with the data.

We have been involved in preparing a software application to be piloted during real surgeries, with the aim of providing surgeons with a simplified interface for combining different data sources, while respecting their current workflow. As part of this effort, we have made use of open-source platforms and contributed back to those projects. This talk will discuss various aspects of this work that are of interest to the broader research software community: interfacing with (medical) hardware; designing GUIs; open-source tools and proprietary libraries; concerns about software that has to run in the operating theatre; and communicating with medical researchers.

  
  
  

**SNAPPY Libraries for Surgical Navigation**

**Stephen Thompson**, Tom Dowrick, Mian Ahmad, Matthew J. Clarkson  
Wellcome/EPSRC Centre for Interventional and Surgical Sciences, UCL

Surgical navigation combines medical imaging, medical image computing, registration, tracking, visualisation, and graphical user interfaces. Researchers working in this area rely on open source platforms that combine functionality in these areas to deliver prototype clinical applications. In this talk I will discuss some of these platforms, and our experiences in using them for clinical application development. I will then introduce the SNAPPY libraries which form a more loosely coupled set of stand-alone open source Python libraries. The SNAPPY libraries are intended to support rapid prototyping of clinical application, faster translation from prototype to approved clinical software, and better dissemination of research.

The established platforms in this field are both large and often difficult to install or compile. It is becoming increasingly hard to recruit researchers with the skills in C++ development to build clinical software using these platforms. SNAPPY is intended to address these problems by providing smaller libraries, written predominantly in Python. Development is accompanied by testing, documentation and quality control to ensure that not only can novel applications be prototyped quickly, but that prototypes can be developed into clinical applications in under two years.

SNAPPY currently consists of 13 libraries providing functionality for visualisation and augmented reality in surgery, together with hardware interface with video, tracking, and ultrasound sources. The libraries are stand-alone, open source, and provide Python interfaces. This design approach enables fast development of robust applications with minimal and well managed dependencies.

  
  
  

#### **Lightning Talks**

  
  
  

**Multiple horses for multiple courses – reliably interfacing programming languages**

**John Lees**, Imperial College London

To make high-quality research software in a time-constrained environment, developers need to use existing libraries. Often, this forces a single choice of language. Allowing developers to instead use the programming language best suited to each module of their software has a number of advantages. But actually deploying a multi-language solution can be challenging – interfaces between languages may require use of technical low-level mechanisms, and installation of software becomes more complex. In this talk I will exhibit some ways to overcome these barriers in multi-language software projects, showing examples combining python machine-learning libraries with C++ memory management. I will also show how package managers such as conda can be set up to glue all of the pieces together, making installation trivial for the majority of users. I will also mention how the use of common scientific data formats such as HDF5 can be advantageous.

  
  
  

**Documentation: Not an API catalogue**

**Mayeul d’Avezac**, Imperial College London

Documenting code is often a post-project afterthought limited to a barely useful catalogue of functions and classes, one after the other. Such catalogues are only useful to those who already know by which end to pick up the code and simply need a refresher on some unlikely detail. I’ll argue that this is a state of mind rather than a necessity. With tools such as doctest, Jupyter notebooks, and Sphinx, we can pull documentation back into the lifecycle of the code, as unit tests, user scenarios and acceptance tests. Documentation comes alive when it is executable and self-validating. Rather than documenting libraries and codes by listing their organs, we can create living documents showing new users how the code can work for them.

  
  
  

**A generic cloud-agnostic platform to support the execution of deadline-constrained workloads**

**Amjad Ullah**, James Deslauriers, Tamas Kiss  
University of Westminster

Scientific research and large-scale commercial applications, e.g. discrete event and agent-based simulations or image/video processing, usually require the execution of large number of jobs, hence result in significant overall execution time. For such applications, cloud environment, with unlimited computational resources, is a natural fit, where they can take advantage of the auto-scaling feature to efficiently use the rented resources. However, there are two key challenges to overcome. Firstly, the existing container management technologies, such as Docker swarm and Kubernetes, do not support job queuing and scheduling. Secondly, the existing auto-scaling offerings facilitate scaling decisions based on either resource usage, such as CPU/Memory utilization; or application performance, e.g. response time, etc. However, such aspects of auto-scaling do not suit the requirements of multi-jobs/batch-based processing applications, where the primary objective is to guarantee the completion of all jobs execution within a specified time limit whilst minimizing system resources usage to reduce cost. Hence, the scaling policies need to consider aspects like length of queue, remaining time to finish all jobs. To address the above-mentioned challenges, i.e. to optimize the deadline-constrained execution of batch-based processing applications, this talk presents the coupling of two autonomous systems titled jQueuer, a container based distributed queuing system, and MiCADO, a multi-cloud orchestration and auto-scaling framework. The synergy between these two systems guarantee the completion of multi-jobs experiment within a desirable time limit, where jQueuer is responsible for the scheduling of jobs and MiCADO deals with the deployment and optimization of computational resources using configurable deadline-based scaling policies.

  
  
  

**Creating scalable, reproducible bioinformatics pipelines with Snakemake and Anaconda**

**Sean Aller**, Adam Witney  
St George’s University of London

Snakemake is a workflow management system that similarly utilises rules to that of GNU make, streamlining the analysis of multiple similar input data. Snakemake workflows on built using a series of rules that define how output files are created from input files. These rules are essentially extensions of python scripts and allow for the running of command-line programs, as well as Python, R and other programming language scripts. The ease of these workflows is their ability to be easily deployed on a variety of systems, ranging from local systems to high-performance computing clusters. This is enabled in part due to the integration of the package manager, anaconda, which allows for the creation of workflow-wide or rule-by-rule virtual environments using configuration files. A use case scenario for this has been the large-scale analysis of clinical isolates from multiple hospitals for rapid detection and identification of antibiotic resistance.

  
  
  

**SHARPy: from a research code to an open-source software tool for the simulation of very flexible aircraft**

**Norberto Goizueta**, Alfonso Del Carre, Arturo Muñoz Simón, Rafael Palacios  
Imperial College London

SHARPy (Simulation of High Aspect-Ratio airplanes in Python) is an nonlinear aeroelasticity simulation tool that permits the analyses of the next generation of aerostructures without using computationally expensive high-order methods or, instead, significant assumptions on the underlying physics.

With the core code written in Python, more intensive routines are in C++ and Fortran, it incorporates efficient multi-language interfaces that enable to share information with minimal cost.

It is built upon a modular framework: the user can interact with the code in a “building block” manner, offering numerous possibilities in the types of analyses that can be performed.

Unlike some research-oriented code, SHARPy is built focused on supporting a growing user base by providing automatic testing and documentation, amongst other tools. This turns a research code into an open-source software for users ranging from students to industrial partners for the simulation of the next generation aircraft and wind turbines.

  
  
  

**Development of the OptimUS library for high-intensity ultrasound propagation**

**Tuomas Koskela** (RITS), Roland Guichard (RITS), David Pérez-Suárez (RITS), Pierre Gelat (Mechanical Engineering), Reza Haqshenas (Mechanical Engineering), Nader Saffari (Mechanical Engineering)  
University College London

We present how we have applied research software engineering skills to the mathematical modelling of high-intensity focused ultrasound propagation in inhomogeneous tissue. OptimUS is a python library developed by researchers at UCL with the goal of releasing it as a tool for researchers and clinicians. We have worked with the research team to apply best practices in research software engineering to the project ahead of its release. Our work has included packaging and refactoring the code, introducing a code review process, setting up automated testing and continuous integration on Travis, building a Docker container for porting the code and developing a Flask graphical user interface to make the library accessible for users who may not be familiar with Jupyter notebooks, the de facto user interface so far. Our work ensures that all scientific code developed meets the highest standards of software architecture and quality assurance.