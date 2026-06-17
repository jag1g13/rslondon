---
layout: single
title: "RSLondonSouthEast 2022: Abstracts"
permalink: /rslse2022/abstracts/
---

[< Back to RSLondonSouthEast 2022: Schedule](/rslse2022/schedule/)

### **Talk Abstracts**

**Keynote**

**Real-time modelling to support outbreak response: the perspective of an academic**  
**Anne Cori**, MRC Centre for Global Infectious Disease Analysis Imperial College London

Through selected examples (including influenza, Ebola and SARS-CoV-2), I will give an overview of the key public health questions modelling can answer to support epidemic response in real-time. I will present some of the challenges associated with real-time modelling, and illustrate how software development can mitigate some of those, highlighting remaining gaps which should be addressed for better epidemic preparedness.

**About the speaker:** Dr Cori is a lecturer in the MRC centre for Global Infectious Diseases Analysis at Imperial College London. She develops statistical methods and tools for the analysis of epidemic data. She is the author of the R package EpiEstim, which has been widely used to monitor transmissibility of SARS-CoV-2 globally. Her research mainly focuses on viruses including Ebola, MERS, influenza and HIV. Over the last two years she has worked mostly on real-time analyses of SARS-CoV-2 transmission and control in England.

**Talk Session 1**

  
  
  

**In-situ visualisation of AMR datasets with OSPRay**

**Miren Radia**, DAMTP, University of Cambridge  
Co-authors:  
Dave DeMarle 1, Amelia Drew 2, James Fergusson 2, Kacper Kornet 2, Paul Shellard 2, Ulrich Sperhake 2  
1 Intel Corporation   2 DAMTP, University of Cambridge

With the advent of exascale on the horizon, there is a pressing need to develop new methodologies in order to exploit its potential. Until recently the dominant approach to visualisation and analysis of outputs from scientific simulations has been post-hoc processing where data saved to disks during the simulation is loaded back into memory and processed accordingly. Unfortunately, the speeds and capacity of HPC file systems have not kept up with the increase in processing power meaning that it is quickly becoming impractical to continue the current post-processing paradigm for the largest datasets. The alternative approach of in-situ processing, where data is processed during the simulation, is becoming more widespread but there is still significant development required in order to bring these in-situ frameworks up to scratch with that of post-processing ones. In collaboration with Intel, we have been developing an in-situ capability for the Adaptive Mesh Refinement (AMR) numerical relativity code GRChombo using ParaView Catalyst. ParaView uses Intel’s OSPRay library (part of its oneAPI Rendering Toolkit) in order to perform ray-tracing for volume rendering. Currently, OSPRay’s support for AMR datasets that are MPI-distributed is limited. In this talk, we will present recent work with Intel to improve this situation and demonstrate our progress with our insitu GRChombo exemplar code.

  
  
  

**The story of Bio Image Operation: An Open-Source cross-platform tool for real-time animal tracking**

**Joost de Folter**, The Francis Crick Institute  
Co-authors: Luke Nightingale

BioImageOperation (BIO) is an Open-Source tool for real-time animal tracking. BIO-B is an additional toolset for behavioural analysis.

BIO was initially developed to extract characteristics of pharaoh ants. The available Open-Source tools did not support modern video formats, tracking of many animals, or real-time processing. From recent review papers on image tracking software, key research and technical requirements have become clear, including a “Call to developers”. The main conclusions were lack of usability, and a gap between software design and intended laboratory use. These have been addressed in the development of BIO. In particular, BIO is Open Source and accessible to the community, cross-platform, supports real-time operation and works with multiple species and many subjects.

BIO is used at Crick for laboratory use, extracting detailed animal behaviour. As part of wider collaboration, it has been applied at the Living Earth Collaborative (USA) to extract characteristic profiles of species and movement behaviour. It also facilitates using open-type low-cost hardware projects (such as Raspberry Pi), and is also being used in Teaching and Research in Natural Sciences for Development (TReND) in Africa (trendinafrica.org).

Supporting Open-Source software, we highly encourage community development using platforms such as github, and in addition technical forums such as image.sc. One of our most important learnings for a successful software project is bridging the cross-domain gap between research and software engineering. We would like to acknowledge Amy Strange (Crick), the Prieto-Godino lab in particular Ruairi Roberts, and the Living Earth Collaborative in particular Brett Seymoure, for their support.

  
  
  

**A computational pipeline for analysis of multi-parameter models: a case study**

**Georgina Al-Badri**, University College London

Computational models involving many parameters, including those based on mathematical models of natural phenomena, require a combination of tools and techniques for effective qualitative and quantitative analysis.

Using a case study of a cell pattern formation model from mathematical biology, my flash talk will outline a few considerations and Python tools to facilitate this process. As a PhD student (recently completed), I was challenged with building a computational pipeline to firstly implement a computational model, and subsequently to enable model analysis and parameterisation.

Using a model containing many parameters required deciding how to best store and access the parameter values (e.g. dictionaries vs. DataClasses), and writing code such that it is compatible with different analyses modules. Two open source modules to conduct parameter sensitivity analysis (SALib), and parameter optimisation using the particle swarm method (Pyswarms), are also suggested.

  
  
  

**Developing an e-Science Centre for the European Plasmasphere, Ionosphere and Thermosphere Research Communities**

**Tamas Kiss**, University of Westminster  
Co-authors: David Chan You Fee1, Gabriele Pierantoni1, Dimitris Kagialis1  
1 University of Westminster

PITHIA-NRF (Plasmasphere Ionosphere Thermosphere Integrated Research Environment and Access services: a Network of Research Facilities) is a project funded by the European Commission’s H2020 programme to build a distributed network of observing facilities, data processing tools and prediction models dedicated to ionosphere, thermosphere and plasmasphere research. One of the core components of PITHIA-NRF is the PITHIA e-Science Centre that supports access to distributed data resources and facilitates the execution of various models on local infrastructures and remote cloud computing resources. The University of Westminster team is responsible for the development of the e-Science Centre within the project.

Resources in the e-Science Centre are registered using a rich set of metadata that is based on the ISO 19156 standard on Observations and Measurements (O&M), and specifically augmented and tailored for the requirements of space physics. When it comes to the execution of Models, the PITHIA e-Science Centre supports three main types of model execution and access scenarios: models can be executed on resources of the various PITHIA nodes, can be deployed and executed on cloud computing resources, or can also be downloaded and executed on the users‚Äô own resources.

This presentation will report on the current state of the development work, after the first year of the project and will also outline the development roadmap. A first prototype of the e-Science Centre is now available supporting resource registration and ontology-based search functionalities. Additionally, proof of concepts of the various execution mechanisms have also been implemented.”

  
  

**Talk Session 2**

  
  
  

**Translation and deployment of medical research software into routine NHS clinical practice**

**Thomas Roberts**, Clinical Scientific Computing, Guy’s and St Thomas’ NHS Foundation Trust

The translation of novel medical research software into routine clinical practice is very challenging. There are many research institutions and companies creating highly innovative solutions to clinical problems, but barriers to clinical translation include (but are not limited to) a lack of understanding of NHS working practices, poor access to relevant clinical stakeholders, lack of knowledge about information governance, poor software validation and verification, and weak patient benefit analysis.

In this presentation, I will discuss the translation of medical research software from two sides: firstly, in my former capacity as an academic researcher and, secondly, now as an AI engineer for the NHS. I will introduce my research into novel fetal magnetic resonance imaging (MRI) methods and discuss how we brought this into routine clinical practice at our hospital. I will discuss the challenges we faced and the achievements we have made during the last 5 years.

Then, I will discuss my current roll in the Clinical Scientific Computing department at Guy’s and St Thomas’ NHS Foundation Trust, where a large part of our remit is facilitating the translation of new AI and software technologies. I will discuss training the clinical AI workforce, how we advise on medical software policy, how we evaluate new AI software proposals, and the software platforms we are developing for the safe deployment of new AI software into the NHS.

This talk will interest researchers or professionals developing medical software for use in clinical practice, particularly imaging software. Attendees can learn about the practicalities of creating software for medical use and insight into the machinations of the wider NHS.

**Speeding up and Parallising R Packages using Rcpp and C++**

**Sherman Lo**, Queen Mary University of London  
Co-authors: Iain Barrass, Queen Mary University of London

The R package poLCA does statistical clustering of polytomous variables. These are variables which have two or more possible outcomes. For example, a survey with multiple-choice questions is polytomous. The R package can be used to group survey results that are similar to each other.

A researcher approached our university’s central RSE group for help with a problem when using poLCA with a large dataset. This dataset contains about half a million data points, each with about two hundred responses. The program would run for an unreasonably long time on our HPC facilities.

We optimise the poLCA package by re-implementing the underlying clustering algorithm (EM algorithm) in C++. The C++ code can be compiled and run using the R package Rcpp. It allows the use of C++ standard libraries (such as , and ) and Armadillo, a matrix library which wraps around LAPACK and OpenBLAS libraries. These provide the basic building blocks for most statistical algorithms.

We observe a 10x speedup with these optimisations. The entire dataset can be processed within minutes using our HPC facilities, making it computationally cheaper and environmentally friendly. The implementation also scales up for larger data, more repetitions and when using more threads.

The talk aims to expose these high-performance tools to attendees and present the process of optimising poLCA. This shall be done by providing small examples of speed-up using Rcpp and explaining the tools, libraries and techniques used in the optimisation of poLCA.

**Imperial College research computing and data science training**

**Katerina Michalickova**, Research Computing and Data Science Team, Graduate School, Imperial College London  
Co-authors: Chris Cooling 1, John Pinney 1, Jianliang Liam Gao 1, Jeremy Cohen 2  
1 Research Computing and Data Science Team, Graduate School, Imperial College London   2 Department of Computing, Imperial College London

This lightning talk will discuss our work and efforts related to upskilling the Imperial community in research computing and data science.

I will introduce Research Computing and Data Science Programme in Imperial College Graduate School. The Programme team consists of five teaching fellows with background in science, who deliver short (3-6 hours) courses to students, researchers and staff.

Together with our external collaborators (RSEs and GTAs), we currently offer courses in 30 topics. The last academic session, we delivered over 130 course instances to an audience of nearly 3000. We also teach an undergraduate module in research computing to cross-departmental cohort of second years undergraduates. The team members are also connected to local and cross-institutional training activities such as the Software Carpentry.

Imperial’s training model is different from that of other institutions. We have found a home at the teaching side of the College, and we are separated from the RSE and HPC groups. There are positive aspects to this as training is seen as an activity in its own right, and the team are given resources to improve teaching skills. On a negative side, we are organisationally apart from our community of practice and have to be extra proactive to stay in touch.

I would like to use this talk to attract anyone interested in training activities to chat afterwards.

**RSE at Cambridge – Ancient and Modern Revised**

**Christopher Edsall**, University of Cambridge

The University of Cambridge is a large, research focused institution. Surely there’s lots of research software engineering going on. In this talk we’ll cover the wider RSE community at Cambridge, the RSE team within Research Computing Services and the new activities of the Cambridge Open Exascale Lab (COEL) and the Institute of Computing for Climate Science (ICCS).

The RSE community has a mailing list and runs a talk series (as seen on talks.cam.ac.uk ) where we update the local community with tips and tricks and reports on work in progress or recently completed. The digital humanities community is expanding, including recruiting a new RSE this year.

There is a group of RSEs founded by Filippo Spiga embedded in the HPC service. We‚Äôll cover the type of work they do and how that team has leant expertise and effort to two new large RSE teams we are in the process of setting up. The COEL mission is to address the challenges getting codes (of interest to the UK) to run at exascale and there is obviously a large RSE component to that. The ICCS is one of the Virtual Institutes of Scientific Software funded by charitable donation from Schmidt Futures with a particular focus on climate science and the incorporation of machine learning.

This talk will cover the challenges of launching and keeping all those balls in the air.

**Talk Session 3**

**Plotting geospacial data from a database using open source mapping software**

**Paul Heaton**, University of Reading  
Co-authors: Maria Broadbridge, University of Reading

LeafletJS was used in conjunction with Mapbox to plot geospatial data on a Javascript canvas without the need for commercial software such as ARCGis.

A web page was created to link a given dataset with geolocation data to the mapping software using Ajax to dynamically plot information.

From an initial map canvas geolocation, an SQL request is sent dataset containing points within the bounded area is generated. This PHP array is converted into JSON data and sent to the web page, where a built-in Mapbox function translates it into plottable markers.

The system allows for modification of markers, can be extended to show regions and lines on the map and allow display of text, images and other information from the database.

The method was used successfully for archaeological information from the British Museum Antiquities Database containing geospatial data, and, more generally, to display location of data points and other attributes.

**Ultrawideband Radio (UWB) in Augmented Reality (AR) Reality and immersive experiences**

**Elliott Hall**, King’s Digital Lab, King’s College London

This talk will focus on using the Ultrawideband Radio (UWB) in Augmented Reality (AR) for live performance and research engagement. UWB is an accessible and cost-effective way to create indoor, spatially aware immersive and AR experiences.

Beginning with a brief overview of UWB technology, we will use family immersive experience The Digital Ghost Hunt (https://digitalghosthunt.com) — co-created by King’s Digital Lab (KDL) and KIT Theatre (https://www.kittheatre.org/) — as a case study for its use in an immersive experience, focusing on the technical and experience design challenges of integrating the technology, as well as the opportunities for collaborative play it enables. It will also include links to repositories and Gists for practical tips on getting started with making a UWB experience of their own.

**Creating Reusable Apps with Django**

**Adrian D’Alessandro**, Research Computing Service, Imperial College London

Creating web apps is a great way of making research outputs. As a central RSE team we often get requests for this kind of work as it is further away from the typical skillset of a researcher. For many of these, we choose to use Python-Django.

We noticed some elements that were repeated across multiple different apps. As Software Engineers we like to avoid repeating ourselves, so we investigated the best way to implement a re-usable component in a Django App. It turns out Django supports this naturally: any Django app can be imported into any other.

This lightning talk will cover some technical details on how to create a re-usable Django App and a simple example of where we have used this. The example will be for a “passwordless login” system, which is available on GitHub. There will also be an associated blog post covering this in more detail.

**Research software and the COVID-19 real-time response**

**Richard FitzJohn**, RESIDE RSE Team, MRC Centre for Global Infectious Disease Analysis, Imperial College London

The research response to COVID-19 pandemic in the UK has been unprecendented, due to the depth of data availability, complexity of models and demands of analysis in near real-time. I will describe the role of software development in supporting the response of the Centre from the beginning of the response in Janury 2020 through to end of regular reporting more than two years later, at its peak involving over 50 researchers. I will focus on two aspects – distributed data warehousing to connect analysis teams with ever-changing streams of data, and our approach to scaling up epidemiological models leading to the creation of possibly the most detailed compartmental model ever written. Along the way I will highlight how we developed reusable robust frameworks but ensured that researchers were fully in control of ongoing model development, how we used automation to keep everything working seamlessly, and how domain scientists became enthusiatic about test-driven development.

### Posters

- **RSE South: A new regional RSE network in the South of the UK**
- **CSVY: A Python reader/writer for CSV files with YAML header**
- **A Showcase of Work at a Central RSE Team (Queen Mary University of London)**
- **RSE at Cambridge – Ancient and Modern Revised**
- **Speeding up and Parallising R Packages using Rcpp and C++**
- **UCL Advanced Research Computing**