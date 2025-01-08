Web Deployment Automation Tool
Overview
The Web Deployment Automation Tool is designed to streamline the deployment of web applications using Python and Nginx on an Ubuntu server. This tool automates the process of managing server resources, supervising Nginx, and installing necessary dependencies. It is ideal for simplifying web deployment tasks and managing the associated infrastructure more efficiently.

Functional Requirements
1. System Health Monitoring
The tool monitors and displays key server statistics, including:

CPU: Number of cores, usage per core, and total usage.
Memory: Total, used, and available RAM.
Disk: Partition usage and available space.
Network: Interface details, total data sent, and received.
2. Nginx Supervision
The tool provides options to:

Check if Nginx is installed and prompt for installation if necessary.
Start, stop, restart, reload, enable, or disable Nginx.
Validate Nginx configuration syntax using nginx -t.
3. Manage Available Sites
The tool manages web application sites with the following functionalities:

List all available sites from /etc/nginx/sites-available/.
Add a new site by:
Cloning a GitHub repository into /services/<domain-name>.
Generating a corresponding Nginx configuration file based on the site type (HTML, PHP, Java, Python, Node.js).
4. Manage Enabled Sites
It allows you to:

List all enabled sites from /etc/nginx/sites-enabled/.
Enable or disable sites by creating/removing symbolic links from /etc/nginx/sites-available/.
Delete site configurations entirely.
5. Check and Install Dependencies
The tool ensures the following runtimes are installed:

PHP 8.3 + Composer
Java 17
Node.js 22
Flask (Python web framework) It also provides an interactive way to install missing dependencies.
