---
layout: single
title: "RSLondonSouthEast 2020: Posters"
permalink: /rslondonse-2020/posters/
---

[< Back to RSLondonSouthEast 2020: Schedule](/rslondon/rslondonse-2020/agenda/)

### **Posters**

1. **Euphonic: A Python package to Simulate 4D Neutron Datasets**  
   Rebecca Fair, *Science and Technology Facilities Council*
2. **Software development for Emergency Planning, Preparedness and Response in Public Health**  
   Declan Bays, Conor Newcombe, Anna Rance and Hannah Williams  
   *Public Health England*
3. **A primer on front-end JavaScript frameworks**  
   Alex Hill, *Imperial College London*
4. **Research code as a service**  
   Rob Ashton, Jeff Eaton, Rich FitzJohn, Alex Hill, Wes Hinsley and Emma Russell  
   *Imperial College London*
5. **Data Safe Havens in the Cloud**  
   Martin O’Reilly1, Daniel Allen1, Diego Arenas2, Jon Atkins1, Claire Austin3, David Beavan1, Alvaro Cabrejas Egea1,4, Steven Carlysle-Davies5, Ian Carter1, Rob Clarke6, James Cunningham7, Tom Doel8, Oliver Forrest1, Evelina Gabasova1, James Geddes1, James Hetherington1, Radka Jersakova1, Franz Kiraly1, Catherine Lawrence1, Jules Manser1, James Robinson1, Helen Sherwood-Taylor9, Serena Tierney10, Catalina A. Vallejos1,5, Sebastian Vollmer1,4, Benjamin Walden1, Kirstie Whitaker1,11, Warwick Wood1  
   *1 The Alan Turing Institute, 2 University of St Andrews, 3 The British Library, 4 University of Warwick, 5 University of Edinburgh, 6 Corinium Technology Limited, 7 University of Manchester, 8 Code Choreography, 9 RRD Labs Ltd, 10 VVW LLP, 11 University of Cambridge*
6. **Research citing software; software citing research**  
   Diego Alonso Álvarez, *Imperial College London*
7. **Developing ‘Skull Base Navigation’ software for facial nerve surgery**  
   Thomas Dowrick, Jonathan Shapey, Tom Vercauteren, Roland Guichard, Anastasis Georgoulas and Matt Clarkson  
   *UCL*
8. **Deploying and auto-scaling scientific applications in the cloud using Terraform and MiCADO**  
   Resmi Ariyattu, James Deslauriers and Tamas Kiss  
   *University of Westminster*
9. **Can we “Move Fast” without “Breaking Things”?**  
   Peter Schmidt, *Research IT Services, University College London*Keith Gutfreund, *Elsevier Ltd*

### **Poster Abstracts**

  
  
  

**Euphonic: A Python package to Simulate 4D Neutron Datasets**  
Rebecca Fair, *Science and Technology Facilities Council*

The latest neutron spectrometers at the ISIS Neutron and Muon Source are routinely producing 4D datasets that are as large as 0.5TB each, and this large amount of data is quickly becoming overwhelming to users. Simulations can help scientists understand their data, but the modelling codes are not integrated with the analysis software, so they are limited to simulating a small subset of their data using their own bespoke scripts. With a combination of domain knowledge and good software engineering, a Python package is being developed to combat this – Euphonic. It can be used with the analysis software or standalone, and aims to allow efficient and routine simulation of entire datasets.

---

  
  
  

**Software development for Emergency Planning, Preparedness and Response in Public Health**  
Declan Bays, Conor Newcombe, Anna Rance and Hannah Williams  
*Public Health England*

The mass urbanisation of the population, in conjunction with the advancement of rapid travel, has resulted in a dramatic improvement in average living conditions. Yet, it is precisely these conditions that have increased our vulnerability to emerging infectious diseases and biological disasters. Within Public Health England’s Emergency Response Department, software is developed to mathematically model such events and provide a rigorous understanding of their dynamics. Outputs may also grant insight into the best intervention strategies, which can assist with the planning and preparation of responses. Software is also developed to quantify the effectiveness of training given to organisations who respond to these scenarios, providing a mechanism to improve the impact of this training. This poster showcases examples of software that has been designed, developed and utilised within the Emergency Response Department to assist with the planning and preparedness for such scenarios.

---

  
  
  

**A primer on front-end JavaScript frameworks**  
Alex Hill, *Imperial College London*

In the 2019 StackOverflow survey Reactjs was voted the most loved web framework, and the most desired by developers not already using it. A narrow second in both categories was Vuejs, and the widely used Angularjs remained in the top 10.

If you’re not already using one of these, you’re probably wondering whether you should be.

But it can be hard to know where to start with the fast paced JavaScript ecosystem. Single Page Apps, React, flux – this talk will demystify these buzz words and help you navigate the modern JavaScript landscape.

---

  
  
  

**Research code as a service**  
Rob Ashton, Jeff Eaton, Rich FitzJohn, Alex Hill, Wes Hinsley and Emma Russell  
*Imperial College London*

How do you take a piece of constantly evolving research software and deploy it for use as a web application, allowing researchers to continue to develop their software and providing users with a stable platform?

That was the circle we attempted to square working with HIV researchers who wanted to allow public health officials to access their impact estimates at the same time as the researchers were developing them.

In our solution, the researchers developed their research software as an R package. We developed an interface layer exposing a stable interface to this code as an HTTP API, and developed a modern web service around it using Kotlin with a front-end in Vue.js, augmenting the research code with authentication, session management and load balancing queues.

This system was designed to allow the underlying research software to change freely, using automated testing to ensure that the research code could successfully be updated.

We describe what worked well in this architecture, pain points that remained and things that we will change. We report on how users found working with the model (and its scientists) in a series of workshops with over 200 participants, creating a tight feedback loop between research and user.

As researchers move to deliver their research in more varied ways than just the traditional paper, this sort of system will become more useful and more common. While our system is just a prototype, we hope our explorations will help other efforts.

---

  
  
  

**Data Safe Havens in the Cloud**  
Martin O’Reilly1, Daniel Allen1, Diego Arenas2, Jon Atkins1, Claire Austin3, David Beavan1, Alvaro Cabrejas Egea1,4, Steven Carlysle-Davies5, Ian Carter1, Rob Clarke6, James Cunningham7, Tom Doel8, Oliver Forrest1, Evelina Gabasova1, James Geddes1, James Hetherington1, Radka Jersakova1, Franz Kiraly1, Catherine Lawrence1, Jules Manser1, James Robinson1, Helen Sherwood-Taylor9, Serena Tierney10, Catalina A. Vallejos1,5, Sebastian Vollmer1,4, Benjamin Walden1, Kirstie Whitaker1,11, Warwick Wood1  
*1 The Alan Turing Institute, 2 University of St Andrews, 3 The British Library, 4 University of Warwick, 5 University of Edinburgh, 6 Corinium Technology Limited, 7 University of Manchester, 8 Code Choreography, 9 RRD Labs Ltd, 10 VVW LLP, 11 University of Cambridge*

The data science research community frequently encounters a need for:

- Secure environments for analysis of sensitive datasets
- A productive environment for curiosity-driven research
- High performance computing capability

These requirements have, to our knowledge, not yet been realised simultaneously.

Some solutions render research unproductive by making it hard to author new code while engaging with the data, or to experiment with the many software libraries realising new analytical techniques. Others lack access to large scale or specialised compute power such as clusters or GPUs.

This perversely reduces security: researchers route around carefully constructed secure environments to avoid perceived productivity loss, increasing the risk of a breach.

An organisation then lacks a clear inventory of all the datasets it is handling, and the risk profile in terms of consequences and threat actors for each.

The Alan Turing Institute has been developing recommended policies and controls for performing productive research on sensitive data, as well as a cloud-based reference implementation. This comprises:

- Clearly defined sensitivity tiers for handling data, mapping to existing data classification and risk categorisation systems, but adapting and extending these to research activities
- A web-based system for review and classification of datasets, and the allocation of users and datasets to projects
- Automated creation of multiple, independent secure environments, each configured according to the appropriate classification tier for the project

A cloud-based approach to secure infrastructure means deployment and configuration of environments is efficient, reliable and auditable, as well as providing access to scalable high performance computing.

---

  
  
  

**Research citing software; software citing research**  
Diego Alonso Álvarez, *Imperial College London*

Software is a key element on modern research, to the extent that a big part of it will not be possible – or will be much more difficult – without it. There is a strong interest and many initiatives worldwide to ensure that any piece of software – and data – used in research, contributing to papers or in grant applications, is properly accounted for and receives the corresponding credit, including to their creators and contributors.

However, there is a flip side: software often implements algorithms and theory described in research papers and books. Sometimes, this use of existing material is referenced in the documentation or in a paper associated to the software, but the software itself remains largely reference-free, and the sources it uses unaccredited.

In this talk, we briefly discuss two common methods of documenting software that allow the addition of references to your code, namely Sphinx and Doxygen. We then highlight some of the shortcomings of these methods and some desirable features that would make these citations more useful for both the citing software and the cited object. Finally, we present a nascent project of the RSE team at Imperial, the Research References Tracking Tool (R2T2) aiming to fill this gap with the support and contributions from the research software community.

---

  
  
  

**Developing ‘Skull Base Navigation’ software for facial nerve surgery**  
Thomas Dowrick, Jonathan Shapey, Tom Vercauteren, Roland Guichard, Anastasis Georgoulas and Matt Clarkson  
*UCL*

The Skull Base Navigation software tool is being deployed as part of an ongoing facial nerve surgery project at Queen’s Square hospital, providing additional intraoperative data and visualisation to the surgical team during tumor resection.

The software, which has been developed in close collaboration with the clinical team, allows multiple data streams (preoperative CT, intraoperative ultrasound and tool tracking data) to be presented in a clinical friendly UI, which minimises disruption to the existing clinical process, with relevant data stored for post operative processing and analysis.

Proprietary code from device manufacturers has been combined with open source tools for data synchronisation (PLUS) and visualisation (3D Slicer), alongside custom Python code to handle the user interface, data storage and workflow.

---

  
  
  

**Deploying and auto-scaling scientific applications in the cloud using Terraform and MiCADO**  
Resmi Ariyattu, James Deslauriers and Tamas Kiss  
*University of Westminster*

Scientific research software as well as many commercial software applications can hugely benefit from the pay-as-you-go model and resource scalability that cloud computing offers. To facilitate, automate and improve the management of cloud resources and services, a large number of open-source tools exist. MiCADO (Microservices-based Cloud Application-level Dynamic Orchestrator) is an automated deployment, autoscaling and optimisation framework that is based on widely used open source technologies, such as Kubernetes (container orchestration), Prometheus (monitoring) and Occopus (virtual machine orchestration). The modular structure of MiCADO means that components can be easily replaced with alternative technologies on demand. This talk aims to share our experiences when replacing Occopus with Terraform as cloud orchestrator within MiCADO in order to support the execution of applications on a larger variety of commercial clouds (e.g. MS Azure and Google Cloud Engine). The developed solution is utilised to execute large scale evacuation simulation scenarios on cloud resources.

---

  
  
  

**Can we “Move Fast” without “Breaking Things”?**  
Peter Schmidt, *Research IT Services, University College London*Keith Gutfreund, *Elsevier Ltd*

This lightening talk focuses on responsible innovation in software and technologies.
For many years, software technologies have moved at a breath-taking pace with a culture of “move fast and break things”. This has led to some unintended consequences: e.g. privacy violations and job displacements.
It is, therefore, worth investigating if and how development tools and processes contribute to some of these effects. In particular:

- Agile Software Development practices, (e.g. Scrum, Kanban)
- “Minimum viable product” deliveries
- Continuous integration and delivery practices

They are said to be wide spread in the technology sector. Their claim is to help organisations “move fast”. But – do they also “break things”? This lightening talk discusses, how and if the positive claims (“move fast”) of these tools and processes can be substantiated. Furthermore, can we evaluate what the more negative side effects can be (“break things”)?