## On-premises Architecture

Visit the [AWS TCO Calculator](https://awstcocalculator.com/).

### Basic Information

1. Currency: USD
2. Starting environment type: On-premises
3. AWS region: US East (N. Virginia)
4. Servers to compare: Virtual Servers

### Application Details

#### Servers

1. Webservers
    Server Type - Non DB
    App. Name - Web
    # VMs - 6
    # Cores/processor - 4
    Memory (GB) - 24
    VMWare
    Linux

2. Ingestion and data processing service
    Server Type - Non DB
    App. Name - IPDS
    # VMs - 12
    # Cores/processor - 4
    Memory (GB) - 12
    VMWare
    Linux

3. Database - DB
    Server Type - DB
    App. Name - DB
    # VMs - 4
    # Cores/processor - 4
    Memory (GB) - 24
    DB Engine - MySQL
    VMWare
    Linux

4. Service for Analytics and Metrics
    Server Type - Non DB
    App. Name - SAM
    # VMs - 2
    # Cores/processor - 4
    Memory (GB) - 12
    DB Engine - MySQL
    VMWare
    Linux


#### Storage

1. Database storage
    SAN - 16 TB
    Disk Type - SSD
2. Surveillance video  
    Object - 60 TB
    95% accessed infrequently
