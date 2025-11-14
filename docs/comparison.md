# Comparison 

VM managed is smaller and significantly more tedious to use and access. However, a VM is significantly easier to deploy versus a managed database. 
VM's are also cheaper to deploy depending on sizes making ideal for smaller scaled tasks. Managed services are ideal for larger scale operations that come with higher 
costs which are more ideal for commerical use rather than individual use. 

### Small student app
For a small scale student app, a vm-managed database is more ideal due to its smaller scale requirements and lower costs. Assuming the student is using Google cloud using similar specs seen in setup_notes_vm.md, monthly costs would range between 10USD-15USD. 

### Departmental analytics DB
For more professional use, a managed database would be more suitable for security reasons, operational use and maintenace reasons. Managed databases are much more flexible when it comes to managing scaling for services for users and some managed database services have automatic scaling available to adjust for department size. With managed databases, maintenace and clean up is more automatic versus vm-managed databases which would require the user to self manage and update. 


### HIPAA-aligned workload 
For a HIPAA-aligned workload, managed databases would be more suited for its proper regulation and scaling. Managed databases for Hipaa-aligned workloads provide more security measures compared to VM managed databases and provide easier auditing methods.


