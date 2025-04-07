# Project Deployment Guide

This guide provides basic steps for deploying the Next.js frontend and the Python (FastAPI) backend. Specific instructions may vary depending on your chosen hosting providers.

**Deployment Order:** It's generally recommended to deploy the **backend first**, as you will need its public URL to configure the frontend.

## Prerequisites

*   A Git repository hosted on a platform like GitHub, GitLab, or Bitbucket.
*   Accounts on your chosen hosting platforms (e.g., Vercel/Netlify for frontend, Render/Fly.io/AWS/GCP/Azure for backend).
*   A provisioned database (if your backend requires one) accessible from your backend hosting environment.

## Backend Deployment (Python/FastAPI)

Choose a hosting provider that supports Python WSGI/ASGI applications (e.g., Render, Fly.io, Heroku (paid), Google Cloud Run, AWS Elastic Beanstalk/ECS, Azure App Service).

**Example using Render.com (Recommended for simplicity):**

1.  **Push Code:** Ensure your latest backend code (including `requirements.txt` and potentially a `Procfile` or `render.yaml`) is pushed to your Git repository.
2.  **Create New Web Service:** In Render, create a new "Web Service" and connect it to your Git repository.
3.  **Configuration:**
    *   **Root Directory:** If your backend code is in the `backend/` subdirectory of your monorepo, set the "Root Directory" to `backend`.
    *   **Runtime:** Select "Python 3".
    *   **Build Command:** `pip install -r requirements.txt` (Render often detects this automatically).
    *   **Start Command:** Use `gunicorn` or `uvicorn` to run your FastAPI app. A common command using `gunicorn` with `uvicorn` workers is:
        ```bash
        gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:$PORT
        ```
        *   Replace `app.main:app` if your FastAPI app instance is located elsewhere.
        *   `-w 4` specifies 4 worker processes (adjust based on your plan/needs).
        *   `-k uvicorn.workers.UvicornWorker` tells gunicorn to use uvicorn workers for ASGI compatibility.
        *   `-b 0.0.0.0:$PORT` binds to all available interfaces on the port provided by Render via the `$PORT` environment variable.
4.  **Environment Variables:**
    *   Navigate to the "Environment" section of your service on Render.
    *   Add essential backend environment variables (copied from your `.env.example` in the `backend` directory, but using production values):
        *   `DATABASE_URL`: The connection string for your *production* database.
        *   `SECRET_KEY`: A strong, unique secret key for JWT or session security.
        *   `CORS_ORIGINS`: **Crucially**, add the URL(s) of your deployed *frontend* here (e.g., `https://<your-live-frontend-url>`). You might also need `http://localhost:3000` if you want to test your deployed backend with your local frontend during development. Separate multiple origins with commas if your backend framework supports it, or configure accordingly.
        *   Any other API keys or settings needed for production.
5.  **Deploy:** Create the service. Render will pull the code, build it, and deploy it.
6.  **Get URL:** Once deployed, Render will provide a public URL (e.g., `https://your-backend-app.onrender.com`). **Copy this URL.**

## Frontend Deployment (Next.js)

Choose a hosting provider optimized for Next.js (e.g., Vercel (highly recommended), Netlify, AWS Amplify, Cloudflare Pages).

**Example using Vercel (Recommended for Next.js):**

1.  **Push Code:** Ensure your latest frontend code is pushed to your Git repository.
2.  **Import Project:** In Vercel, import the Git repository.
3.  **Configure Project:**
    *   **Framework Preset:** Vercel should automatically detect "Next.js".
    *   **Root Directory:** If your frontend code is in the `frontend/` subdirectory of your monorepo, change the "Root Directory" setting to `frontend`.
    *   **Build & Output Settings:** Usually, Vercel's defaults for Next.js are correct.
4.  **Environment Variables:**
    *   Navigate to the "Settings" -> "Environment Variables" section of your project on Vercel.
    *   Add essential frontend environment variables (copied from your `.env.example` in the `frontend` directory, but using production values):
        *   `NEXT_PUBLIC_BACKEND_API_URL`: **Paste the public URL of your deployed backend here** (e.g., `https://your-backend-app.onrender.com/api/v1` - include the path prefix like `/api/v1` if your backend uses one). The `NEXT_PUBLIC_` prefix makes it available in the browser.
        *   `NEXTAUTH_URL` (if using NextAuth.js): The canonical URL of your *frontend* deployment (e.g., `https://<your-live-frontend-url>`).
        *   `NEXTAUTH_SECRET` (if using NextAuth.js): A strong, unique secret for NextAuth.js session encryption. This is a *server-side* variable for Next.js.
        *   Any other public API keys (`NEXT_PUBLIC_...`) or server-side keys needed.
5.  **Deploy:** Click the "Deploy" button. Vercel will build and deploy your Next.js application.
6.  **Get URL:** Vercel will provide one or more public URLs for your deployed frontend (e.g., `https://your-frontend-app.vercel.app`).

## Post-Deployment

1.  **Testing:** Thoroughly test your live application:
    *   Navigate through pages.
    *   Test login/logout functionality.
    *   Test features that rely on backend data fetching.
    *   Check browser developer console for errors (especially CORS errors if the backend wasn't configured correctly).
2.  **Custom Domains:** Configure custom domains for both your frontend and backend through your hosting providers' dashboards and your DNS provider. Remember to update `CORS_ORIGINS` on the backend and `NEXTAUTH_URL` (if applicable) on the frontend if you switch to a custom domain.
3.  **Monitoring & Logging:** Set up monitoring and logging services to track application health and diagnose issues in production. Most hosting platforms offer some built-in logging.

---

This provides a solid starting point. Remember to consult the specific documentation for your chosen hosting providers for more detailed instructions and advanced configuration options.