---
layout: single
title: "RSLondonSouthEast 2023: Abstracts"
permalink: /rslondonsoutheast2023/abstracts/
---

[< Back to RSLondonSouthEast 2023: Schedule](/rslondonsoutheast2023/schedule/)

### **Talk Abstracts**

**Talk Session 1**

**Research code as a service**

**Robert Ashton**, RESIDE, MRC Centre for Global Infectious Disease Analysis, Imperial College London  
Co-authors:  
**Rich Fitzjohn, Emma Russell, Alex Hill, Wes Hinsley, Lekan Anifowoshe, Mantra Kusumgar**  
*RESIDE, MRC Centre for Global Infectious Disease Analysis, Imperial College London*

How do you take a piece of constantly evolving research software and deploy it for use as a web application, allowing researchers to continue to develop their software whilst providing users with a stable platform? How do you know that a new version of the research software will work reliably within the existing application? And how do you keep the web bits out of the research software so that scientists can keep focused on their research questions? In our solution, we developed an HTTP API as a stable interface layer between the research code and the web code. This allows scientists to use their preferred languages and libraries, whist also allowing web developers to use modern web frameworks and technologies. This system was designed to allow the underlying research software to change freely. We ensure we can integrate the components reliably through automated testing, JSON schema validation and continuous deployment. We describe what worked well in this architecture, pain points that remained and things that we will change. We report on how users found working with the model (and its scientists) in a series of workshops with over 200 participants, creating a tight feedback loop between research and user. As researchers move to deliver their research in more varied ways than just the traditional paper, this sort of system will become more useful and more common. We’ve implemented this pattern in several applications with different front-end and back-end languages, and we hope our explorations will help other efforts.

**Building ‘good enough’ digital workflows in the field**

**Stuart Grieve**, Queen Mary University of London  
Co-authors:  
**Harry Owen1, Milto Miltiadou1, Emily Lines1**,  
1 *University of Cambridge*

Like many scientific disciplines, environmental science relies on increasingly large and complex datasets, the analysis of which require a combination of domain expertise and specialist computational skills. However, unlike many other disciplines, much environmental science data collection and analysis takes place in remote locations, without access to the internet, HPC systems, or tech support. This talk will detail the challenges of collecting, managing and processing large volumes of environmental data over several months of fieldwork in Spanish, Polish and Finnish forests. Over the course of several years, we have collected high resolution 3D point cloud data of forest structure from ground-based and airborne laser scanners, alongside aerial photography and ecological measurements. Through this process we have confronted issues of reproducibility, offline data management, instrument failure and conflicting proprietary workflows. We contrast these approaches with ideas of ‘best practice’ and identify a series of lessons that can be applied to future data-intensive fieldwork, in addition to providing valuable perspective for non-field based research.

**Pre-Processing Android Application PacKages (APKs) for Static Analysis at Scale – A lesson learned from developing AppInspect**

**Jason Chao**, University of Siegen

This talk will share a lesson learned from the development of AppInspect – a research tool enabling nontechnical researchers to study Android apps. The talk will focus on AppInspect’s technique of preprocessing Android PacKage (APKs) for static analysis at scale. The pre-processing enables the mining of thousands of Android apps for the reuse of code and resources, questionable system calls, suspicious libraries and their evolution.

An APK is essentially a ZIP archive that contains a collection of files. An Android app is a set of filesof different elements, such as code, icons, images, and user interfaces. Extracting elements from an APK using existing tools creates a deep hierarchy of directory structure. The overhead of files lookup in a directory is costly, and the I/O performance of most file systems decreases as the number of files increases. The use of existing tools alone to work with a large number of APKs would be very inefficient and take a long time to run an analysis.

The author finds that pre-processing the files within an APK is key to enabling the efficient processing of researchers’ queries. AppInspect transforms the diverse files within an APK into a tabular format based on Apache Parquet, which is optimised for storing a huge amount of data for the purpose of analysis. A key advantage of the technique is compatibility with major big data analytics tools, support of different data types, and optimised for use in distributed computing infrastructure.

**Supporting research collaboration in the Plasmasphere, Ionosphere, Thermosphere research communities via the PITHIA e-Science Centre**

**Tamas Kiss**, University of Westminster  
Co-authors:  
**1David Chan You Fee, 1Dimitris Kagialis, 1Gabriele Pierantoni, 1Gabor Terstyanszky**,   
1 *University of Westminster*

PITHIA-NRF (Plasmasphere Ionosphere Thermosphere Integrated Research Environment and Access services: a Network of Research Facilities) integrates data, models and physical observing facilities for further advancing European research capacity in this area. A central point of PITHIA-NRF is the PITHIA e-Science Centre (PeSC), a science gateway developed by the University of Westminster team, that provides access to distributed data sources and prediction models to support scientific discovery.

Although shortly presented in an earlier RSL workshop, the PITHIA e-Science Centre has now mature significantly, reaching its first official public release. This presentation and live demonstration will provide an overview of the current status and capabilities of the PeSC, highlighting the underlying ontology and metadata structure, the registration process for models and datasets, the ontology-based search functionalities and the interaction methods for executing models and processing data.

Besides supporting the core PITHIA research community (partners in the PITHIA-NRF EU funded project – https://pithia-nrf.eu/), the PeSC is now also accepting requests from external communities. The first such community is represented by the ARCAFF – Active Region Classification and Flare Forecasting EU project (https://arcaff.eu/) that now targets integration with the PeSC to publish and make available its datasets and models for the larger space physics community. Challenges related to this integration will also be covered.

**Talk Session 2**

**Forging RSE skills pathways**

**Diego Alonso Álvarez**, Imperial College London  
Co-authors:  
**1Aleksandra Nenadic1, Aman Goel2, Dave Horsfall3, Eli Chadwick4, Hannah Williams5, Iain Barrass6, Lieke de Boer7, Martin O’Reilly8, Matthew Bluteau9, Nadine Spychala10, Paul K Korir11, Sean Marshallsay12**  
1 *Software Sustainability Institute, University of Manchester*,   2 *University of Manchester*,  3 *Newcastle University*,  4 *The Carpentries*,  5 *UK Health Security Agency*,  6 *University of Glasgow*,  7 *Netherlands eScience Center*,  8 *Alan Turing Institute*,  9 *UK Atomic Energy Authority*,  10 *University of Sussex*,  11 *University College Cork*,  12 *Playtech BGT Sports*

Forge RSE Skill Development Pathways is a resource to support RSEs (Research Software Engineers) in tracking and managing their professional development. It also helps RSE team leaders to identify gaps in the skills of their team, to guide strategic decisions on recruitment and to support existing team members to develop themselves.

Forge RSE comprises an RSE competency framework, outlining a structured set of skills that are useful when working as an RSE, with examples of how these skills can be demonstrated at different levels of experience (not all RSEs will or need to have all skills at all levels); a curated set of training resources, linked to the skills and levels from the competency framework; and tools to visualise and compare different competency profiles.

This is a work in progress with many opportunities to provide support and input. So get in touch if you want to be involved: <https://github.com/RSEToolkit/training>

**‘Active’ Storage: deep data storage solutions from the ExCALIStore project**

**Sadie Bartholomew & Valeriu Predoi**, University of Reading and National Centre for Atmospheric Science (NCAS)  
Co-authors:  
**George O’Brien1, Jeff Cole1, Grenville Lister1, Bryan Lawrence1, Neil Massey2, Jack Leland2**

1 *University of Reading and National Centre for Atmospheric Science*,   2 *Centre of Environmental Data Analysis and Science and Technology Facilities Council*

In an ideal world, dataset users will not need to know or worry about details regarding the processing of their data, for example whether their data is being analysed on their local machine or on a remote server. Therefore a client application should be able to make that decision on behalf of the user and instigate the work at the most appropriate location.

In this talk, we outline progress so far from our ExCALIStore project, part of the ExCALIData project under the ExCALIBUR programme, which recognises the difficulties that users have in managing the location of their data across tiered storage, and of configuring their workflows to take advantage of newly available acceleration options and aims to make it simpler for the user to focus on the work at hand. The user simply runs their normal code and benefits from greater efficiency (in terms of wallclock time and data transfer energy) as and when it is available. By using an analysis client package that imports PyActiveStorage, data is analysed with minimal data transfers, but the analysis workflow itself doesn’t change. Rather, the computational steps are optimised in three dimensons now, with location being added, as an optimisation dimension to the ubiquitous time, and memory.

**Superseding R packages – lessons learned from transitioning to {epichains} from {bpmodels}**

**James Azam**, London School of Hygiene and Tropical Medicine

Occasionally, R package developers might decide to supersede their packages with a new implementation to reflect their evolved thinking and experiences in package design. Examples include {ggplot2} and {reshape2}. In multiple contributor projects, this often comes with non-trivial decisions, including name changes, deprecations, and the preservation of git histories. These decisions are non-trivial, especially in epidemiology and public health where reproducibility is a key consideration. {bpmodels}, an R package for analyzing infectious disease data, is currently in the same situation. {bpmodels} was independently developed in 2019, but the Epiverse-TRACE Initiative, which aims to develop an interoperable ecosystem for outbreak analytics, now provides the capacity to maintain it. This involves a re-imagination of the package, including a name change to {epichains}, planned integration of existing and new functionalities, and object-oriented programming. This talk will highlight some conundrums faced during this process, which is ongoing, and provide the opportunity for mutual learning.

**Building Operational Research Tools with a User-Friendly GUI Using Free Cloud-Hosted Jupyter Notebook: A Case Study of TikTok Video Analysis**

**Jason Chao**, University of Siegen  
Co-authors:  
**Elena Pilipets**, *University of Siegen*

The lightning talk will illustrate the story of building the research tool “Video Frame and Audio Extractor” in a week based on a free cloud-based Jupyter Notebook, and making the tool user-friendly for non-technical researchers studying TikTok videos.

One of the authors initially faced challenges in extracting frames from a large number of videos using ffmpeg’s command-line interface, which was hardly usable by researchers without technical expertise. The challenge hampers non-technical researchers’ agency in studying TikTok videos.

In preparation for a workshop on studying TikTok videos at Digital Methods Winter School 2023, the authors used a freely available cloud-hosted Jupyter Notebook to build a tool with a graphical user interface that invokes ffmpeg to extract frames from videos. The tool was built, tested and made operational within a week. Participants in the workshop, who are mostly without technical backgrounds, found the new tool easy to use, and their agency in researching TikTok videos increased.

The lightning talk discusses the design of the “”Video Frame and Audio Extractor”” tool and highlights the potential of using free cloud-hosted Jupyter Notebooks for building operational research tools with a graphical user interface quickly.

**Towards substantiable dashboards for open-source software projects**

**Yagmur Idil Ozdemir**, Advanced Research Computing Centre, UCL  
Co-authors:  
**Miguel Xochicale1, Stephen Thompson2**  
1 *Advanced Research Computing Centre, UCL*, 2 *Department of Medical Physics and Biomedical Engineering, UCL*

Making the code of research understandable, replicable, and sustainable for a wider community can lead to impact beyond research funding cycles. Open-source tools under Astropy and ROpenSci stem from research communities that collaboratively develop code and methods to advance research in these fields. Defining sustainable software in this context can involve code quality, ease for contribution and user activity. However, these criteria can be subjective and pose challenges to effectively measure and monitor as technologies change. Community dashboards, like used by Astropy and ROpenSci, can consolidate such information and monitor the long-term research impact. Our team in the Advanced Center for Research Computing at UCL has collaborated with researchers to develop more sustainable tools within Scikit-Surgery (a python-based open-source library for surgical navigation). The Scikit-Surgery dashboard consolidates key indicators of software sustainability, such as code coverage and documentation, enabling users to make informed choices. Our current aim as Research Software Engineers is to improve the deployment and current state of this dashboard with the vision of sharing its model with a wider community. During this presentation, we will delve into the deployment of a dashboard with the current metrics and their significance. We will highlight our ongoing efforts to enhance these metrics to provide more valuable insights to the users, bring open questions for discussions, and a survey to interact with the audience. We will also present our approach to share this deployment as a template, which would allow researchers from different fields to create their own sustainability dashboards. The resources of this work are available at <https://github.com/SciKit-Surgery/scikit-surgery-stats>.

**Using HTMX for front-end web development**

**Christopher Cave-Ayland**, Imperial College London

For some time Single Page Applications (SPAs) have been the dominant paradigm for the development of professional and interactive web pages. Many well recognised frameworks such as React, AngularJS and Vue.js support the development of SPAs.

Increasingly however the SPA model is being critiqued for its technical complexity, expense and slow development speeds. A number of projects are aiming to provide simpler alternatives. Of these, htmx (https://htmx.org/) is of particular note as it has been chosen as part of the 2023 cohort of the GitHub Accelerator program.

Htmx focuses on extending HTML to trigger requests to the application back-end under a much wider variety of circumstances. The back-end then returns snippets of html that are substituted into the web page. This simple concept allows your web application to be composed almost entirely of HTML with a set of htmx provided attributes applied.

Web development is a common activity for RSEs and often we have to balance creating a compelling user experience with a constrained complexity budget. Htmx provides a attractive alternative to technically complex SPA frameworks that can be quickly and easily adopted. This talk will provide a brief overview of htmx, some notable applications and our (very early) experimentation in it’s usage.