### Local Deployment
1. **Fork or Clone the Repository**:
   You can view or clone the repository directly from the following link:  
   [DreramScapes GitHub Repository](https://github.com/monicathomas8/Dreamscapes)

2. **Install Dependencies**:
   - Install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```

3. **Set Up Environment Variables**:
   - Create a `.env` file in the root of your project and add the following variables:
     ```
     SECRET_KEY=your_secret_key
     DEBUG=True
     DATABASE_URL=sqlite:///db.sqlite3
     ```

4. **Run Migrations**:
   - Apply migrations to set up the database:
     ```bash
     python manage.py migrate
     ```

5. **Collect Static Files**:
   - Collect static files locally to ensure they are ready for production:
     ```bash
     python manage.py collectstatic
     ```
   - This gathers all CSS, JavaScript, and image files into the `staticfiles` directory.

6. **Run the Project Locally**:
   - Start the development server:
     ```bash
     python manage.py runserver
     ```

---

### Heroku Deployment

1. **Push Code to GitHub**:
   - Ensure all changes are committed and pushed to GitHub:
     ```bash
     git add .
     git commit -m "Prepare for Heroku deployment"
     git push origin main
     ```

2. **Log In to Heroku**:
   - Log in to your Heroku account:
     ```bash
     heroku login
     ```

3. **Create a New Heroku App**:
   - Create a new app on Heroku:
     ```bash
     heroku create <your-app-name>
     ```

4. **Set Up Environment Variables**:
   - Go to the Heroku dashboard for your app.
   - Under the **Settings** tab, click **Config Vars** and add:
     - **Key:** `PORT` | **Value:** `8000`
     - **Key:** `SECRET_KEY` | **Value:** your_secret_key
     - Add your database URL if using a PostgreSQL database.

5. **Set Buildpacks**:
   - Add Python as the first buildpack.

6. **Connect to GitHub**:
   - In the Heroku dashboard, go to the **Deploy** tab.
   - Under **Deployment Method**, select **GitHub**.
   - Connect your GitHub repository.

7. **Deploy the Application**:
   - Choose a deployment method:
     - **Automatic Deployment**: Automatically deploy on new commits to the main branch.
     - **Manual Deployment**: Click **Deploy Branch** to deploy manually.

8. **Access the Application**:
   - Once deployment is complete, open the app using the URL: