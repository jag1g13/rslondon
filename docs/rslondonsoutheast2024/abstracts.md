---
layout: single
title: "RSLondonSouthEast 2024: Abstracts"
permalink: /rslondonsoutheast2024/abstracts/
---

[< Back to RSLondonSouthEast 2024: Schedule](/rslondonsoutheast2024/schedule/)

### **Talk Abstracts**

**Talk Session 1**

****A custom transpiler for flexible code generation****

**James Knight**, University of Sussex

Code generation is a popular way to allow scientific software written in compiled languages such as C++ to be customised by its users. It is particularly useful when targeting hardware such as GPUs where approaches such as embedding scripting languages or customisation by runtime polymorphism are unsuitable.

Our GeNN spiking neural network simulation library is written in C++ and currently uses the simplest form of code generator: the user defines neuron models in C code which is preprocessed, combined with boilerplate code provided by GeNN and passed to the OpenCL/CUDA compiler. This approach enables heterogeneous models to be fused into a single kernel, allowing GeNN to minimise kernel launches and improve performance. However, this simple approach has drawbacks in terms of user experience and security and only offers limited scope for the analysis and transformation of the user code.

Here we describe the C++ transpiler we have developed to replace GeNN’s simple code generator. Both for backwards compatibility and because we believe it is a sensible abstraction for describing performant numerical code, user code is still provided in a subset of C but it is now scanned and parsed into an abstract syntax tree (AST). The AST is then type-checked and ‘pretty printed’ back into OpenCL/CUDA code for compilation. In future, we intend to build on this framework to enable the vectorization required to exploit half-precision arithmetic on NVIDIA GPUs, the folding of constants known at code generation time, automatic differentiation and targeting of FPGA-based programmable accelerators.”

**OpenGHG – A community platform for greenhouse gas data analysis**

**Prasad Sutar**, University of Bristol  
Co-authors:  
**Matt Rigby1, Rachel Tunnicliffe1, Gareth Jones1, Brendan Murphy1, Christopher Woods1**  
1 *University of Bristol*

To address the urgent need to understand changes in greenhouse gas  
(GHG) emissions, there has been dramatic growth in GHG measurement  
and modelling systems in recent years. However, this growth has led to  
substantial challenges; to date, there has been little standardisation of data  
products, and the interpretation of GHG data requires combined informa-  
tion from numerous models.

OpenGHG is a platform that offers data retrieval from various public  
archives, data standardisation, and researcher-friendly data analysis tools.  
It helps researchers overcome the challenges posed by independent networks,  
archival standards, and varying spatial and temporal scales in greenhouse  
gas research. OpenGHG has an internal set of standards into which different  
data formats are converted. It offers data analysis and visualisation tools, a  
Jupyter Notebook interface, and will offer options for both cloud and local  
installations. Additionally, to handle large data we have employed the Zarr  
storage system for efficient file storage handling.

In this presentation, a demonstration of OpenGHG is being used in the  
development of a prototype “operational” emissions evaluation system for  
the UK, the Greenhouse gas Emissions Measurement and Modelling Ad-  
vancement (GEMMA). This system will combine bottom-up (inventory-  
based) and top-down (observation-based) approaches to evaluate emissions  
in near-real time. An attempt will be made to shed light on some of the  
challenges faced and associated success stories that occurred during the de-  
velopment of this flexible and extensible community-led software to tackle  
scientific and technical challenges.

**Lab Management: Strategic integration of technical teams**

**Pamela Mellen**, King’s College London

After 7 years of refining RSE software development processes, our team increasingly identified a critical new role: “Lab Manager”. A core responsibility of this role is to integrate the Lab into the broader institutional research strategy. This requires establishing a dynamic awareness of, and involvement in, conversations at all levels—faculty, university, funder, and beyond. Constant horizon scanning ensures we identify challenges and opportunities, aligning RSE team activities with wider strategies, shaping new initiatives, and embedding best practices.

Though many teams may not have a dedicated Lab Manager, recognising the importance of engagement—and accepting that not everyone will have the expertise or capacity to be involved—is vital. My Lab Manager remit requires understanding the team’s research interests and goals, being aware of past project activities, and identifying synergies and opportunities to capitalize on them.

This talk initiates a discussion on the importance of engagement and enabling staff involvement. It emphasises the need to allocate time for activities outside the team’s core work and introduces new priorities. How can strategic integration be facilitated? What roles are best suited to incorporate it? How can we ensure engagement supports the entire team, regardless of which individuals take an active part?

**Enhancing Community Engagement and Contribution through the R Development Guide**

**Saranjeet Kaur Bhogal**, Imperial College London

The R Development Guide (R Dev Guide) is a resource designed to onboard new contributors to the R project, making the transition smoother and more accessible. Initially drafted in 2021 with the support of the R Foundation, the guide has undergone significant revisions, notably during the Google Season of Docs 2022. The presentation will cover the guide’s evolution and its role in fostering a more inclusive and collaborative environment.

Attendees (seasoned or new contributors to R) will gain insights into leveraging the R Dev Guide for effectively contributing to the R project and/or for further enhancements to the guide itself. The session aims to develop attendees’ skills in navigating the R project and collaborating with a global community.

The evolution of the guide reflects a broader commitment to fostering an inclusive community and democratising the process of contributing to the R project. It would provide a pathway for attendees seeking to contribute to open-source and engage with the global R community. This presentation will help start discussions on continuous learning and community collaboration within software development.

*A poster will also be on display to support this talk.*

**Talk Session 2**

**Solar Alchemy: Transforming Magnetic Field Data In Space With Lossless Compression**

**Edward Fauchon-Jones**, Imperial College London  
Co-authors:  
**Alastair Crabtree**, *Imperial College London*

Solar Orbiter is a pioneering European Space Agency spacecraft studying never before observed aspects of the Sun including the Sun’s polar regions, as it becomes one of the closest Sun observatories. The onboard Magnetometer instrument (MAG) records magnetic field vectors that help us understand not only how the Sun behaves, but also how it interacts with out planet.

While one of the most precise magnetometers ever made, the accuracy of MAG has degraded over time. Operational workarounds have mitigated this degradation so far, but these workarounds are imperfect and disruptive.

Separately to this issue, a project was initiated to add a feature to the software that controls MAG to enable lossless compression of the magnetic field data before being transmitted back to Earth. MAG can vary the cadence at which magnetic field vectors are recorded. Compression will enable MAG to record and transmit at higher cadences for longer.

This talk will present the lossless compression algorithm that enabled a nearly 2x increase in MAG vectors for the same allocated data transmission volume, and how additionally this algorithm was able to provide a production solution to the accuracy degradation. While presented in the context of magnetic field data, this algorithm is valuable more generally for compressing time series data in low resource compute environments.

The project’s outcome was more successful and more useful than anticipated, however there were plenty of failures and wrong paths taken along the way. This talk will also highlight these unsuccessful aspects and share lessons learned that are valuable for the wider research software community.

**Swarmchestrate – Application-level Swarm-based Orchestration Across the Cloud-to-Edge Continuum**

**Tamas Kiss,** University of Westminster  
Co-authors:  
**Amjad Ullah1, Jozsef Kovacs1, James DesLauriers1**

1 *University of Westminster*

A Cloud-to-Edge orchestration system is responsible for the automation of application deployment and their runtime management by providing simultaneous access to the heterogeneous resource landscape of the computing continuum. Most currently available orchestration tools are based on a centralised execution model. Such a model, while relatively easy to implement, carries several disadvantages. For example, a single point of failure, an easy target for security attacks, and the central controller can be easily overloaded as the system scales. Furthermore, the centralised execution model is not a natural fit considering the distributed and dynamically changing nature of the cloud-to-edge computing continuum. To address these challenges the Swarmchestrate EU-funded research project aims to create a completely decentralised, autonomous, secure and self-organised application orchestration system by combining and extending emerging technologies, such as Swarm computing, distributed AI, distributed ledger systems and decentralised identity management. The approach applied by Swarmchestrate is fundamentally new to application orchestration and its emergence will be important for research relying on high performance computing that can benefit from the different layers of the dynamic computing continuum.

**Integrated data management for highly collaborative and multi-omics projects**

**Mike Gavrielides**, The Francis Crick Institute

In this talk, we will briefly describe how we tackle data management for a large data-intensive project. TracerX EVO is a multi-omics project that will endeavor to bring a deeper understanding of cancer evolution, prevention, diagnosis and treatment. It is a highly collaborative project which involves multiple NHS hospitals and research centres including the Francis Crick Institute, CRUK and UCL.

The project involves patient recruitment, sample collection, process and shipment, high throughput data generation like sequencing, imaging and others, data storage, data sharing and data analysis. Such projects are extremely data-intensive and it’s crucial to have robust and effective data management to guarantee successful outcomes.

The platform we have built provides hospitals and research centres with an integrated collaborative environment that will streamline scientific processes, enable easy data access, mitigate human errors associated with obsolete practices and enhance security. It supports the management of clinical data for patients (recruitment and consent), effective sample data capture and tracking, shipment tracking and data integration between different systems. It provides a central space that collates all data together and APIs to allow analysis pipelines to interact with data effectively. Additionally, it supports easy data sharing with collaborators and complies with FAIR and GCP.

*A poster will also be on display to support this talk.*

**ReCoDE – A Collection of Exemplar Programming Projects for Cognitive Apprenticeship**

**Chris Cooling**, Imperial College London  
Co-authors:  
**Ryan Smith**, *Imperial College London*

The Research Computing and Data Science (RCDS) team at the Graduate School of Imperial College London have partnered with the Imperial RSE team to produce a series of exemplar programming projects – Research Computing and Data Science Exemplars (ReCoDE). These projects are designed to be learning resources for postgraduate students and early career researchers. Each exemplar is an accessible, complete scientific computing project annotated for efficient learning.

The exemplars come from various disciplines, and each is created by a Graduate Teaching Assistant (GTA) in collaboration with a member of RCDS staff and an RSE. Each GTA is asked to design a learning experience around a program that solves a real problem in their area of expertise. The exemplars contain best practice approaches and tools, applied in a realistic way.

The RCDS team member provides pedagogical support, ensuring the learning experience is cohesive, accessible, and effective. The RSE team provides programming support, ensuring the code is of a high quality and that best practices are used throughout. The approach is not prescriptive, and we encourage the GTAs to describe their decision-making process to illustrate why specific design choices were made. During the process, the GTAs enhance their teaching, software engineering and project management skills.

ReCoDE complements the RCDS courses, which impart technical content. The ReCoDE exemplars do not teach the specifics of programming (such as how to create an array in NumPy or compile a Fortran script). Instead, the exemplars show how to combine many different tools and skills to create a cohesive and realistic project. This is designed to use cognitive mentorship pedagogical technique to bridge the gap between theoretical learning provided by courses and the demands of building practical research projects.

This summer, we will partner with students to begin an advertisement campaign for students, supervisors, and teaching staff.

**Environmentally-aware use of GitHub Actions**

**Diego Alonso Álvarez**, Imperial College London  
Co-authors:  
**Adrian D’Alessandro1, Alex Dewar1, Chris Cave-Ayland1, Daniel Cummins1, James Turner1, Ryan Smith1, Sahil Raja1, Saranjeet Kaur Bhogal1, Tom Bland1**  
1 *Imperial College London*

The use of GitHub Actions – and similar platforms – for continuous integration and deployment (CI/CD) facilitates the adoption of quality assurance and testing tools in an automated manner, in turn resulting in better quality software and more productive collaboration. However, in the end, all these tools need to run in servers located somewhere, consuming energy in the process. While the convenience and power of these tools is indisputable, the configurations used are often redundant, running an unnecessary range of scenarios that add very little value, if any, to the knowledge on the quality and correctness of the software being analysed. In this talk we discuss some of the steps that can be taken to make a more rational use of GitHub Actions for CI/CD, as well as tools and techniques that can be used to monitor and reduce the energy usage.

### Posters

**Responsible AI assessment and development: centring communities in requirements elicitation**

**Samantha Callaghan**, King’s College London; **Abdenour Bouich**, University of Glasgow  
Co-authors:  
**Paul Gooding1, Rosie Spooner1, Arianna Ciula2, Miguel Vieira2, Tiffany Ong2, Kirsten Thorpe3, Lauren Booker3, Robin Wright4**  
1 *University of Glasgow*2 *King’s Digital Lab, King’s College London*3 *Jumbunna Institute for Indigenous Education & Research, University of Technology Sydney*4 *Digital Preservation Coalition*

This poster will introduce a project investigating responsible use and design of AI systems in libraries that seek to include knowledge from specific communities. Although guidelines for community specific data governance and community-centred AI design exist, in libraries there has been little application of these principles and a lack of engagement with communities and digital research technical professionals (RTPs).

We will address the need for clear guidance on responsible AI systems assessment and development that embeds community rights and perspectives into the ethical principles of trustworthy AI. The project will scope the knowledge by which memory institutions, including libraries, can: reconnect communities with their knowledge; foster relationships between RTPs and communities; and co-develop or critique AI systems collaboratively and responsibly.

We will integrate this knowledge into an inclusive requirements elicitation process for community engagement in the assessment and development of AI systems via an actionable, pragmatic and scalable model.

This submission will promote the role of digital RTPs in centring particular communities in the AI requirement elicitation process when the data being used is from those communities. The poster will be of particular interest to those working with such data and processes.

**Presenting a Workflow of Automating UI software Testing and Reviewing a Commercial Case Study**

**Amalie Shi**, Adaptix

Verifying the performance and safety is at the heart of the medical software release process. At Adaptix, we have developed a flat-panel x-ray tomosynthesis device that performs rapid diagnostic imaging. The device emits x-rays at different angles and reconstructs the images to a high-resolution 3D images to facilitate medical diagnosis. The product utilizes a software UI that is designed with a workflow in mind to streamline the user experience. It can be a laborious task to repetitively test the software UI by manually clicking the buttons. By using a python package called PyWinAuto, I was able to automate the user’s behaviors to perform the image acquisitions for thousands of times without manually clicking the UI buttons. Often, the software development goes in tandem with the automation script where the names of the buttons are fixed by having defined them in the source code. By locking down the names of the buttons in the source code at the early stage of the software development, the automation scripts could be integrated into the continuous development process even when the software gets updated. Automating the UI workflow can significantly reduce the testing effort and allow more aggressive edge case testing. By presenting the strategic methods of streamlining the automation process, I hope to present a new way of performing software usability testing.

**Integrating XIOS into the neXtSIM-DG next-generation sea ice model**

**Joe Wallwork**, Institute of Computing for Climate Science, University of Cambridge  
Co-authors:  
**Tom Meltzer1, Marion Weinzierl1, Tim Spain2, Einar Ólason2**  
1 *Institute of Computing for Climate Science (ICCS), University of Cambridge*2 *Nansen Environmental and Remote Sensing Center (NERSC), Bergen, Norway*

neXtSIM-DG is a next-generation sea-ice model written in C++, developed as part of the Scale-Aware Sea Ice Project (SASIP). This poster documents our team’s work on integrating the XIOS (XML input-ouput server) library into neXtSIM-DG, giving it the ability to read and write to files in an asynchronous, parallel and efficient manner. Whilst XIOS is written in C++, its primary user base is the climate modelling community, who typically couple to it through a Fortran interface. We evaluate the benefits brought by this integration, as well as discussing the challenges associated with such coupling efforts. These challenges include implementing new backends within code bases of considerable size, deciding how much of the library to integrate, and coupling to codes in an unintended manner.

**The HPC and RSE Experience Programme**

**Adrian D’Alessandro**, Research Computing Service, Imperial College London

The Imperial College Research Computing Service is running a programme that will create a pathway into RSE and HPC careers. This program is called the HPC and RSE Experience Programme and is a six month job for Early Career Researchers wanting to dip their toes in the world of HPC and RSE. This program gives them exposure to working as an RSE and working alongside the HPC sys admins and user support staff. We are enthusiastic about this programme, it is a great training and career development opportunity for the participants and it expands the pool of RSE and HPC-aware researchers in the wider community. We have run three iterations of this and the fourth one will be starting a couple of months after RSECon24. We would like to use this poster as an opportunity to discuss ideas with the community to improve the structure of the programme and encourage other RSE groups to run similar programmes.

**STEP-UP: A Strategic TEchnical Platform for University technical Professionals**

**Samantha Ahern1, Michael Bearpark2, Arianna Ciula3, Jeremy Cohen2, James DesLauriers4, James Graham3, Tamas Kiss4, Pamela Mellen3, Tiffany Ong3, James Wilson1, Victoria Yorke-Edwards1**  
1 *UCL*2 *Imperial College London*3 *King’s College London*4 *University of Westminster*

STEP-UP is a new UKRI-EPSRC-funded Strategic Technical Platform that will build upon the regional Research Software London community to develop new regional Communities of Practice supporting digital Research Technical Professionals (dRTPs) in areas including software, data and research computing infrastructure. STEP-UP will be undertaking a range of activities from developing a structured training programme to support dRTPs and help them to enhance their skills, to setting up mentoring and secondment schemes. The project team will also be working to enhance career opportunities for dRTPs by engaging with key stakeholders and advocating for improved structures, policies and institutional strategies. The poster will provide an introduction to STEP-UP and the activities that the project will be undertaking over the coming years.