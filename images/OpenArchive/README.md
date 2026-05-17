# Open Archive - Student Document Management System

Open Archive is a comprehensive Django-based document management system designed specifically for educational institutions to manage student records, files, and program tracking with robust security, automated backups, and data synchronization capabilities.

## 🚀 Key Features

### 📁 Document Management
- **Student File Storage**: Upload and organize student documents with automated file naming
- **Document Type Management**: Customizable document categories with folder organization
- **File Versioning**: Track document changes and maintain audit trails
- **Bulk Upload**: Efficient batch processing of multiple student files
- **Advanced Search**: Find documents by student, program, term, or document type
- **File Security**: Role-based access control with secure file storage

### 👥 Student & Program Management
- **Student Records**: Complete student information management with unique identifiers
- **Program Tracking**: Multi-program support with flexible term structures
- **Term Assignments**: Automatic student-term assignment management
- **Program Progression**: Track student progress through program terms
- **Custom Labels**: Configurable field labels for institutional branding

### 🔐 Security & Access Control
- **Role-Based Permissions**: Granular access control (Admin, Supervisor, Staff, etc.)
- **Secure Authentication**: Django's built-in security with password protection
- **Audit Logging**: Comprehensive logging of all system activities
- **Data Privacy**: FERPA-compliant student record protection
- **Session Management**: Secure user sessions with timeout controls

### 🔄 Data Synchronization
- **SQL Database Integration**: Sync data from external sources (SQLite, PostgreSQL, MySQL)
- **Programs Update**: Automated program data synchronization
- **Terms Update**: Term information updates from external systems
- **Students Update**: Student record synchronization with validation
- **Flexible Update Modes**:
  - Create Only: Add new records, skip existing
  - Update Only: Update existing records, skip new
  - Create and Update: Comprehensive synchronization
  - Replace All: Complete data refresh (use with caution)
- **Dry-Run Mode**: Test synchronization without making changes

### 💾 Backup & Recovery
- **Automated Backups**: Scheduled daily backups of database and media files
- **Flexible Backup Configuration**: Choose what to include (database, media, or both)
- **Retention Management**: Automatic cleanup of old backup files
- **Backup Verification**: Integrity checking of backup files
- **Easy Restoration**: Simple restore process from backup files
- **Cloud Storage Ready**: Compatible with cloud storage solutions

### 📊 Task Management & Automation
- **Unified Task System**: Centralized management of all automated tasks
- **Flexible Scheduling**: Daily task execution at specified times
- **Task Types**:
  - Backup Tasks: Database and media file backups
  - Data Update Tasks: External data synchronization
  - Custom Tasks: Extensible framework for new task types
- **Task Actions**:
  - **Test Run**: Safe testing of task configurations
  - **Force Run**: Immediate execution regardless of schedule
  - **Activate/Disable**: Easy task management
- **Comprehensive Logging**: Detailed execution logs and statistics

### 📈 Reporting & Analytics
- **System Logs**: Detailed activity tracking and audit trails
- **Task Statistics**: Execution metrics and success/failure tracking
- **Data Import Reports**: Synchronization statistics and error reporting
- **User Activity**: Track user actions and system usage
- **Performance Metrics**: System health and performance monitoring

### 🎨 User Interface
- **Clean Admin Interface**: Intuitive Django admin with custom enhancements
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Dynamic Forms**: Context-sensitive form fields based on selections
- **Bulk Operations**: Efficient batch processing of records
- **Advanced Filtering**: Powerful search and filter capabilities
- **Custom Branding**: Configurable labels and institutional customization

## 🛠 Technical Specifications

### Core Technology Stack
- **Backend**: Django 4.x (Python web framework)
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **Frontend**: Django Admin with custom templates and CSS
- **File Storage**: Local filesystem with cloud storage options
- **Authentication**: Django's built-in auth system
- **Security**: CSRF protection, SQL injection prevention, XSS protection

### Database Support
- **Primary**: SQLite (built-in, no setup required)
- **External Sync**: PostgreSQL, MySQL, additional SQLite databases
- **Connection Types**: Direct database connections with secure credential management
- **Data Validation**: Comprehensive field validation and error handling

### File Management
- **Storage**: Organized directory structure with automatic folder creation
- **Naming**: Intelligent file naming with conflict resolution
- **Types**: Support for all common document formats (PDF, DOC, JPG, PNG, etc.)
- **Size Limits**: Configurable upload size limits
- **Security**: Secure file access with permission checking

### System Requirements
- **Python**: 3.8 or higher
- **Django**: 4.0 or higher
- **Database**: SQLite (included) or PostgreSQL/MySQL
- **Storage**: Minimum 1GB for application, additional for file storage
- **Memory**: Minimum 512MB RAM (2GB+ recommended)

## 📋 Installation & Setup

### Quick Start
```bash
# Clone the repository
git clone https://github.com/yourusername/CSI_SchoolDocs2.0.git
cd CSI_SchoolDocs2.0

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Set up database
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

### Production Deployment
- Supports standard Django deployment options
- Compatible with Apache, Nginx, Gunicorn
- Environment-based configuration
- SSL/HTTPS support
- Static file serving optimization

## 🔧 Configuration Options

### Task Management
Configure automated tasks through the admin interface:
- **Backup Tasks**: Schedule, retention, inclusion options
- **Data Sync Tasks**: Connection strings, SQL queries, update modes
- **Custom Tasks**: Extensible framework for additional functionality

### Security Settings
- User roles and permissions
- Session timeout configuration
- File access restrictions
- Audit logging levels

### System Customization
- Institution-specific labels
- Custom document types
- Program and term structures
- File organization schemas

## 📚 Management Commands

### Data Synchronization
```bash
# List available data update tasks
python manage.py update_data --list-tasks

# Run program updates with dry-run
python manage.py update_data programs --dry-run

# Custom student sync
python manage.py update_data students \
  --connection-string "sqlite:///external.db" \
  --query "SELECT * FROM students" \
  --update-mode create_update

# Run all scheduled tasks
python manage.py run_tasks

# Force run specific task
python manage.py run_tasks --task-id 1 --force
```

### Backup Management
```bash
# Manual backup
python manage.py perform_backup --test

# Force backup regardless of schedule
python manage.py perform_backup --force

# Custom retention period
python manage.py perform_backup --retention-days 30
```

## 🔄 Workflow Examples

### Daily Operations
1. **Student File Upload**: Staff upload student documents through the admin interface
2. **Automatic Organization**: Files are automatically categorized and stored
3. **Data Sync**: External student data is synchronized during off-hours
4. **Backup Creation**: Daily backups ensure data protection
5. **Progress Tracking**: Student progress through programs is monitored

### Administrative Tasks
1. **User Management**: Create and manage user accounts with appropriate permissions
2. **Program Setup**: Configure programs, terms, and document types
3. **Task Scheduling**: Set up automated backups and data synchronization
4. **System Monitoring**: Review logs and task execution statistics
5. **Data Maintenance**: Manage retention policies and archive old records

## 🚨 Error Handling & Troubleshooting

### Common Issues
- **File Upload Errors**: Check file size limits and permissions
- **Sync Failures**: Verify database connections and SQL query syntax
- **Backup Issues**: Ensure adequate storage space and write permissions
- **Permission Errors**: Review user roles and access rights

### Logging & Monitoring
- **System Logs**: Available through Django admin interface
- **Task Execution**: Detailed logs for all automated tasks
- **Error Tracking**: Comprehensive error reporting and resolution guidance
- **Performance Monitoring**: System health and usage statistics

## 🔐 Security Best Practices

### Data Protection
- Regular security updates
- Encrypted connections for database sync
- Secure file storage with access controls
- Regular backup verification
- User activity monitoring

### Access Control
- Principle of least privilege
- Regular user access reviews
- Strong password requirements
- Session management
- Audit trail maintenance

## 📞 Support & Maintenance

### Regular Maintenance
- **Database Optimization**: Regular maintenance for optimal performance
- **Storage Management**: Monitor and manage file storage usage
- **Security Updates**: Keep Django and dependencies current
- **Backup Verification**: Regular testing of backup and restore procedures
- **Performance Monitoring**: Track system performance and usage patterns

### Extensibility
- **Custom Task Types**: Framework for adding new automated tasks
- **API Integration**: Potential for REST API development
- **Custom Reports**: Extensible reporting system
- **Third-party Integration**: Plugin architecture for external systems
- **Custom Fields**: Flexible field management for institutional needs

## 📄 License & Compliance

### Educational Use
- Designed specifically for educational institutions
- FERPA compliance considerations built-in
- Student privacy protection mechanisms
- Audit trails for compliance reporting

### Data Retention
- Configurable retention policies
- Automated cleanup procedures
- Compliance reporting capabilities
- Secure data disposal options

## 🚀 Future Enhancements

### Planned Features
- **REST API**: Full API for external integrations
- **Mobile App**: Dedicated mobile application
- **Advanced Analytics**: Enhanced reporting and dashboard features
- **Cloud Integration**: Native cloud storage providers support
- **Multi-tenancy**: Support for multiple institutions
- **Document OCR**: Automatic text extraction from documents

### Integration Opportunities
- Student Information Systems (SIS) integration
- Learning Management System (LMS) connectivity
- Identity provider integration (LDAP, Active Directory)
- Cloud storage services (AWS S3, Google Drive, etc.)
- Notification systems (email, SMS)

## 📞 Getting Help

### Documentation
- **User Guides**: Step-by-step instructions for common tasks
- **Admin Manual**: Comprehensive administration guide
- **API Documentation**: Technical integration documentation
- **Troubleshooting**: Common issues and solutions

### Support Resources
- **Issue Tracking**: GitHub issues for bug reports and feature requests
- **Community Forum**: User community for questions and discussions
- **Professional Support**: Available for enterprise deployments
- **Training Services**: User training and system administration courses

---

**Open Archive** - Empowering educational institutions with comprehensive document management and student tracking capabilities.

*Built with Django • Secure • Scalable • Educational-focused*
