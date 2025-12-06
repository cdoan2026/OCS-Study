# 🚀 Deployment Guide - Making Your Visualizations Public

This guide explains how to make your OCS Study Abroad visualizations publicly accessible using **GitHub Pages**.

## 📋 Prerequisites

- The repository is pushed to GitHub
- You have admin access to the repository

## 🌐 Option 1: GitHub Pages (Recommended - FREE)

GitHub Pages is a free hosting service that serves static websites directly from your GitHub repository.

### Step 1: Make Your Repository Public (if it's private)

1. Go to your repository on GitHub: `https://github.com/cdoan2026/OCS-Study`
2. Click on **Settings** (⚙️ icon in the top right)
3. Scroll down to the **Danger Zone** section
4. Click **Change visibility**
5. Select **Make public**
6. Confirm by typing the repository name

> **Note:** If you want to keep the repository private, GitHub Pages for private repos requires a GitHub Pro account. Alternatively, see other deployment options below.

### Step 2: Enable GitHub Pages

1. In your repository, go to **Settings** → **Pages** (in the left sidebar)
2. Under **Source**, select:
   - **Branch:** `claude/visualization-programs-countries-01HK8WM8HoUqoanJq6rMaGmP` (or merge to main first)
   - **Folder:** `/ (root)`
3. Click **Save**
4. Wait 1-2 minutes for the deployment to complete

### Step 3: Access Your Public Dashboard

After deployment, your visualizations will be available at:

```
https://cdoan2026.github.io/OCS-Study/
```

Or if you have a custom domain configured:
```
https://your-custom-domain.com/
```

The main dashboard will automatically load at:
```
https://cdoan2026.github.io/OCS-Study/visualizations/index.html
```

### Step 4: Share the Link

Once deployed, you can share this link with anyone:
- **Main Dashboard:** `https://cdoan2026.github.io/OCS-Study/`
- **Direct to Visualizations:** `https://cdoan2026.github.io/OCS-Study/visualizations/index.html`

---

## 🔧 Option 2: Netlify (Alternative - FREE)

Netlify offers easy deployment with continuous integration.

### Quick Deploy

1. Go to [netlify.com](https://www.netlify.com/)
2. Sign up with your GitHub account
3. Click **Add new site** → **Import an existing project**
4. Select **GitHub** and authorize Netlify
5. Choose the `OCS-Study` repository
6. Configure build settings:
   - **Base directory:** leave empty
   - **Build command:** leave empty (static site)
   - **Publish directory:** leave empty or use `/`
7. Click **Deploy site**

Your site will be live at: `https://random-name-12345.netlify.app`

You can customize the subdomain or add a custom domain in Netlify settings.

---

## 🌟 Option 3: Vercel (Alternative - FREE)

Vercel is another excellent option for hosting static sites.

### Quick Deploy

1. Go to [vercel.com](https://vercel.com/)
2. Sign up with your GitHub account
3. Click **Add New** → **Project**
4. Import the `OCS-Study` repository
5. Configure:
   - **Framework Preset:** Other
   - **Root Directory:** leave as default
   - **Build Command:** leave empty
   - **Output Directory:** leave empty
6. Click **Deploy**

Your site will be live at: `https://ocs-study.vercel.app`

---

## 📱 Option 4: Custom Web Hosting

If you have your own web hosting (e.g., university server, shared hosting):

1. **Export the visualizations:**
   ```bash
   cd /home/user/OCS-Study
   zip -r ocs-visualizations.zip visualizations/ index.html .nojekyll
   ```

2. **Upload to your web server:**
   - Use FTP/SFTP to upload the files
   - Or use your hosting provider's file manager
   - Upload to your `public_html` or `www` directory

3. **Access via your domain:**
   - `https://yourdomaon.com/visualizations/`

---

## 🔒 Option 5: Password-Protected Hosting

If you want to keep some access control:

### Using Netlify with Password Protection

1. Deploy to Netlify (see Option 2)
2. In Netlify dashboard, go to **Site settings** → **Access control**
3. Enable **Visitor access** → **Password protection**
4. Set a password
5. Share the URL and password with authorized users

### Using Vercel with Password Protection

Vercel requires a Pro plan for password protection.

---

## ✅ Recommended Approach

For DePauw University's OCS program, I recommend:

1. **GitHub Pages** - Best for:
   - Complete public access
   - Free hosting
   - Easy to maintain
   - Automatic updates when you push to the branch

2. **Netlify** - Best for:
   - Need password protection (free tier)
   - Want custom domain with SSL
   - Need continuous deployment

---

## 🔄 Updating Your Visualizations

When you update the data or visualizations:

### For GitHub Pages:
1. Run `python3 create_visualizations.py` to regenerate
2. Commit and push changes:
   ```bash
   git add .
   git commit -m "Update visualizations with new data"
   git push origin claude/visualization-programs-countries-01HK8WM8HoUqoanJq6rMaGmP
   ```
3. GitHub Pages will automatically redeploy (takes 1-2 minutes)

### For Netlify/Vercel:
1. Run `python3 create_visualizations.py`
2. Commit and push changes
3. Netlify/Vercel will automatically rebuild and deploy

---

## 📊 Monitoring & Analytics

To track who's viewing your visualizations:

### Google Analytics
1. Create a Google Analytics account
2. Get your tracking ID
3. Add the tracking code to `visualizations/index.html`

### Netlify Analytics
- Available in Netlify dashboard (paid feature)
- Shows page views, unique visitors, bandwidth

---

## 🆘 Troubleshooting

### GitHub Pages Not Working?

**Problem:** 404 error after enabling GitHub Pages
- **Solution:** Wait 2-3 minutes for initial deployment
- **Solution:** Check that `.nojekyll` file exists (prevents Jekyll processing)
- **Solution:** Make sure the branch and folder are correctly selected

**Problem:** CSS/JS not loading
- **Solution:** Check that all paths in HTML files are relative (not absolute)
- **Solution:** Ensure `.nojekyll` file is present

**Problem:** Repository is private
- **Solution:** Make repository public OR upgrade to GitHub Pro

### Netlify Issues?

**Problem:** Build fails
- **Solution:** No build command needed for static sites - leave empty
- **Solution:** Make sure publish directory is set to `/` or empty

---

## 📧 Need Help?

If you encounter any issues:
1. Check the [GitHub Pages documentation](https://docs.github.com/en/pages)
2. Check the [Netlify documentation](https://docs.netlify.com/)
3. Contact your IT department for university hosting options

---

## 🎉 You're All Set!

Once deployed, your interactive visualizations will be accessible to:
- Students exploring study abroad options
- Faculty advisors helping students choose programs
- Administration for strategic planning
- Anyone interested in DePauw's study abroad data

**Share your dashboard link and help students make informed decisions about studying abroad!** 🌍✈️📚
