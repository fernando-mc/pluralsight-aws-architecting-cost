## On-premises Architecture

Visit the [AWS TCO Calculator](https://awstcocalculator.com/).

### Basic Information

1. Currency: USD
2. Starting environment type: On-premises
3. AWS region: US East (N. Virginia)
4. Servers to compare: Physical Servers

### Application Details

#### Servers

1. Webservers
    Server Type - Non DB
    App. Name - Web
    # Processors/server - 1
    # Cores/processor - 4
    # Servers - 6
    Memory (GB) - 24

2. Ingestion and data processing service
    Server Type - Non DB
    App. Name - IPDS
    # Processors/server - 2
    # Cores/processor - 4
    # Servers - 12
    Memory (GB) - 12

3. Database - DB
    Server Type - DB
    App. Name - DB
    # Processors/server - 2
    # Cores/processor - 4
    # Servers - 48
    Memory (GB) - 128
    DB Engine - MySQL

4. Service for Analytics and Metrics
    Server Type - Non DB
    App. Name - SAM
    # Processors/server - 2
    # Cores/processor - 6
    # Servers - 2
    Memory (GB) - 12


#### Storage

1. Rolling backups
    NAS - 4 TB
2. Database storage
    SAN - 16 TB
    Disk Type - SSD
3. Surveillance video segments  
    Object - 120 TB
    95% accessed infrequently