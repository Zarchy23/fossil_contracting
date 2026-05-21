# Fossil Contracting Admin Dashboard Guide

## Overview

The Fossil Contracting website features a **custom admin dashboard** built to replace Django's default admin panel. This dashboard provides an intuitive interface for managing all your website content.

### Dashboard Access

**URL:** `http://localhost:8000/dashboard/`

### Default Admin Credentials

- **Username:** `admin`
- **Password:** `admin123`

⚠️ **Security Note:** Change your password immediately after first login. These are default credentials for development only.

---

## Dashboard Features

### 1. Main Dashboard (`/dashboard/`)

The main dashboard displays quick statistics:

- **Total Projects:** Number of projects in the system
- **Blog Posts:** Number of published blog posts
- **Unread Feedback:** Count of unread anonymous messages
- **Statistics:** Number of company statistics

Quick action buttons allow you to:

- ➕ Add a new project
- ✍️ Write a new blog post
- 📊 Create a new statistic

---

## Project Management

### access Projects (`/dashboard/projects/`)

View all projects in a table format showing:

- Project name
- Location
- Project status (Planning/Ongoing/Completed/On Hold)
- Completion percentage (visual progress bar)
- Project value in USD
- Featured status (shown with ⭐ icon)
- Edit and Delete buttons

### Add a New Project (`/dashboard/projects/create/`)

Fill in the following fields:

- **Project Name** * (required)
- **Location** * (required)
- **Client** (optional)
- **Description** (optional - up to 5000 characters)
- **Value (USD)** (numeric value of project)
- **Status** (Planning, Ongoing, Completed, or On Hold)
- **Completion (%)** (0-100)
- **Start Date** (date picker)
- **End Date** (date picker, optional)
- **Image URL** (path to project image)
- **Featured Project** (checkbox - shows on homepage if checked)

### Edit a Project (`/dashboard/projects/<id>/edit/`)

Click the "Edit" button on any project to modify its details. All fields can be updated except the creation date.

### Delete a Project (`/dashboard/projects/<id>/delete/`)

Click the "Delete" button to remove a project. You'll need to confirm the deletion on a confirmation page.

⚠️ **Warning:** Deletion is permanent and cannot be undone.

---

## Blog Management

### View Blog Posts (`/dashboard/blog/`)

See all blog posts with:

- Post title
- Author name
- View count (number of times read)
- Like count
- Pinned status (indicated with 📌 icon)
- Publication date
- Edit and Delete buttons

### Create a Blog Post (`/dashboard/blog/create/`)

Write a new blog post with:

- **Post Title** * (required)
- **Content** * (required - main post text, supports up to 50,000 characters)
- **Author** (name of the author, optional)
- **Pin This Post** (checkbox - pins important posts to the top)

### Edit a Blog Post (`/dashboard/blog/<id>/edit/`)

Update any existing blog post. Changes are saved immediately.

### Delete a Blog Post (`/dashboard/blog/<id>/delete/`)

Remove a blog post permanently. All associated comments will also be deleted.

---

## Feedback Management

### View Feedback (`/dashboard/feedback/`)

See all anonymous feedback with:

- **Type** (Complaint, Suggestion, Praise, Bug Report, etc.)
- **Message** (truncated preview)
- **Date** (when submitted)
- **Status** (Unread/Read)
- Read and Delete buttons

The dashboard shows **unread count** at the top. Unread feedback is highlighted with a blue background.

### Feedback Types

- 🔴 **Complaint:** Customer complaints
- 🔵 **Suggestion:** Improvement suggestions
- 🟢 **Praise:** Positive feedback
- 🟡 **Bug Report:** Technical issues

### View Feedback Details (`/dashboard/feedback/<id>/`)

Click "View" to see the complete feedback message and details:

- Full message text
- Feedback type
- Submission date and time
- Current read status
- Option to delete

Reading a feedback entry automatically marks it as read.

### Delete Feedback (`/dashboard/feedback/<id>/delete/`)

Remove feedback permanently after confirming on the confirmation page.

---

## Company Statistics

### View Statistics (`/dashboard/stats/`)

See all company statistics displayed in a table:

- **Label** (e.g., "Projects Completed")
- **Value** (the number)
- **Icon** (Font Awesome icon)
- **Suffix** (e.g., "+" for "+250")
- **Order** (display order on website)

### Add a Statistic (`/dashboard/stats/create/`)

Create a new company statistic:

- **Label** * (e.g., "Projects Completed")
- **Value** * (e.g., "250")
- **Icon** (Font Awesome icon code, e.g., "fas fa-briefcase")
- **Suffix** (e.g., "+")
- **Display Order** (lower numbers appear first)

### Find Font Awesome Icons

Visit **https://fontawesome.com/icons** to browse available icons.

Use the icon code format:

- Solid icons: `fas fa-icon-name`
- Brand icons: `fab fa-icon-name`
- Regular icons: `far fa-icon-name`

**Examples:**

- `fas fa-briefcase` - Briefcase icon
- `fas fa-chart-bar` - Chart icon
- `fas fa-wrench` - Wrench icon
- `fab fa-github` - GitHub logo

### Edit a Statistic (`/dashboard/stats/<id>/edit/`)

Update any statistic. Changes reflect immediately on your website.

### Delete a Statistic (`/dashboard/stats/<id>/delete/`)

Remove a statistic permanently.

---

## Navigation

### Sidebar Menu

The left sidebar provides quick access to all sections:

- 🏠 **Dashboard** - Main overview
- 💼 **Projects** - Project management
- 📰 **Blog** - Blog post management
- 💬 **Feedback** - Anonymous feedback
- 📊 **Statistics** - Company stats
- 🚪 **Logout** - Sign out

The current section is highlighted in green.

### Responsive Design

The dashboard is fully responsive and works on:

- Desktop computers (full sidebar visible)
- Tablets (optimized sidebar)
- Mobile phones (collapsible navigation)

---

## Tips & Tricks

### Best Practices

1. **Always fill required fields** (marked with *)
2. **Use meaningful project names** - easier to identify in listings
3. **Set realistic completion percentages** - helps track progress
4. **Pin important blog posts** - featured posts appear first
5. **Respond to feedback** - even if not directly in the dashboard, acknowledge important messages
6. **Organize statistics by order** - lower numbers display first on the homepage

### Common Tasks

**Adding a completed project:**

1. Go to Projects
2. Click "Add New Project"
3. Fill in details
4. Set Status to "Completed"
5. Set Completion to "100%"
6. Check "Featured Project" if it's notable
7. Save

**Publishing an important announcement:**

1. Go to Blog
2. Click "Write New Post"
3. Enter title and content
4. Check "Pin This Post"
5. Save

**Filtering Feedback:**

The feedback view shows all messages. Use your browser's search (Ctrl+F) to find specific feedback.

---

## Troubleshooting

### Can't Log In

**Problem:** Username/password not working

**Solution:**

- Verify the username is `admin`
- Check that you're using the correct password
- Clear browser cookies and try again
- Contact the site administrator if credentials were changed

### Form Won't Submit

**Problem:** Form stays on the same page after clicking Save

**Solution:**

- Check that all required fields (marked with *) are filled
- Look for error messages below each field
- Ensure dates are in the correct format (YYYY-MM-DD)
- Try using a different browser

### Changes Not Showing

**Problem:** Changes made in dashboard don't appear on the website

**Solution:**

- Refresh your browser (Ctrl+F5)
- Clear your browser cache
- Wait a few seconds - changes are applied immediately but may require page refresh
- Check that all required fields are properly filled

### "You do not have permission"

**Problem:** Getting permission error

**Solution:**

- You must be logged in as a staff member
- Contact the site administrator to enable admin access
- Try logging in again

---

## Security

### Password

- Change the default password immediately
- Use a strong password (mix of letters, numbers, special characters)
- Don't share your admin credentials
- Log out when finished

### Access Control

Only staff members can access the dashboard. Non-staff user accounts cannot log in.

### Data Safety

- **Backups:** The system automatically creates backups
- **Deletions are permanent:** Always confirm before deleting data
- **Audit trail:** All changes are timestamped and can be reviewed

---

## Logging Out

Click the **Logout** button in the sidebar to end your session.

After logout:

- You'll be redirected to the login page
- Your session data is cleared
- You'll need to log in again to access the dashboard

---

## Need Help?

For additional support:

1. Check this guide again - most issues are covered
2. Contact the technical team
3. Visit https://docs.djangoproject.com/ for Django documentation

---

## Updates & Changes

The dashboard is regularly updated with new features:

- **Feature requests:** Contact your administrator
- **Feedback:** We welcome suggestions for improvements

---

**Last Updated:** {{ current_date }}

**Dashboard Version:** 1.0
