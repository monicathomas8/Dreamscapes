# DreamScapes E-commerce Platform
A unique platform blending art and technology to bring dream-like landscapes to life.

## About
DreamScapes is an e-commerce platform designed to offer unique, unframed A4 art prints inspired by dream-like landscapes. The project integrates technical functionality with artistic creativity to deliver a seamless shopping experience.
live site is here: [DreamScapes](https://dreamscapes-4bf65f774d22.herokuapp.com/)

To test use card: 4242 4242 4242 4242 

![website](static\images\screens.png)

## User Experience Design

### 1. Strategy
- Focused on simplicity, accessibility, and aesthetic appeal to ensure a smooth user experience.
- Designed to align with the needs of art enthusiasts seeking high-quality, customizable art.

### 2. Target Audience
- Art enthusiasts in the UK.
- Customers who prefer clean, simple designs and personalized options.

---

## Planning

### 1. Wireframes
- Wireframes created to map out the structure and flow of the website.
- Tools used: Balsamiq
![wireframe mock up](static\images\wireframe.png)

### 2. Design
- Designed using Bootstrap for responsiveness and cohesive layout. Finished with a personal style CSS.

### 3. Lucid Board
- Utilized Lucidchart to visualize user journeys and workflows.
![planning](static\images\luicd.png)
---

## Business Model
DreamScapes operates with a robust and customer-centric business model designed to provide value through artistic excellence, seamless functionality, and strong brand engagement. Here's a detailed breakdown:
1. Revenue Streams
DreamScapes generates revenue through multiple channels:
2.  Direct Art Sales: Selling high-quality A4-sized prints of dream-like landscapes and symbolic pieces. Each artwork is unframed, ensuring affordability and easy customization for the buyer.
3.  Custom Orders: Offering personalized orders where customers can request specific dimensions, themes, or designs. This premium service adds an exclusive touch and caters to unique customer needs.
4. Future Opportunities:- Premium pricing for framed artwork options.
5. Expanding into digital downloads for artwork that can be printed at home.

- **Web Marketing:** 
SEO optimization, email campaigns via Mailchimp, and targeted social media presence to increase visibility and engagement.
FaceBook Page
![Facebook Page](static\images\faceboopage.png)
MAilChimp Sign Up 
![mailchimp](static\images\mailchimp.png)
---

## Technologies Used

### 1. Languages
- Python, HTML, CSS, JavaScript

### 2. Frameworks and Libraries
- Django, Bootstrap

### 3. Databases
- SQLite, PostgreSQL

### 4. Other Tools
- Stripe for payment integration
- Cloudinary for media storage
- Heroku and GitHub for hosting

## 4. Other Tools
- Heroku (Deployment)
- GitPod (Development environment)
- GitHub (Version control)
- W3C Validator (HTML and CSS validation)
- PEP8 (Python code validation)
- Favicon.io  [Favicon Generator](https://favicon.io/)
---
## Features

### 1. Design
- A streamlined, visually appealing user interface with artistic touches.

**Landing Page**
![DreamScapes Home Page](static\images\homepage.png)

**Art Shop**: A grid display of availabile.
![Art Shopp Page](static\images\artshop.png)

 **Art Detail**: A page that loads the full artwork with more detils.
![Art detail Page](static\images\artdetail.png)

 **FAQs**: An FAQs page to help shoppers. 
![Art detail Page](static\images\faqs.png)

- **Responsive Design**: Fully responsive for an optimal experience across devices. These include:

   1. Navbav - adaptive for different screen sizes, with a toogle button and dropdown menu.
    ![Navbar dropdown menu](static\images\navbar.png)
   2. Footer with social links. 
   ![footer ](static\images\footer.png)
   3. Pop up messages
   ![pop up message](static\images\popup.png)
 
### 2. Colour Scheme
- Calming blues and purples to evoke serenity.

### 3. Imagery
- Dream-like landscapes and unframed A4 art prints. All Images were personally created. 

---

## Information Architecture

### Project Structure
<pre>
DreamScapes/
├── dreamscapes/         # Project
├── home/                # Home app (landing page, FAQ, contact form)
├── artworks/            # Artworks app (browse, search, and view artwork)
├── orders/              # Orders app (place, view, and manage orders)
├── users/               # Users app (authentication and profile management)
├── templates/           # HTML templates
├── static/              # CSS, JavaScript, and images
├── media/               # Uploaded images (artwork previews)
├── manage.py            # Django management script
├── db.sqlite3           # SQLite database (development)
└── requirements.txt     # Project dependencies
</pre>

###  Database
- A well-structured database to store user, order, and artwork information.

### Entity-Relationship Diagrams
please note; some modifactions were made during the development process. 

#### 1. User Model (Users App)
Represents the users of the site, including admins and customers.

**Fields**:
- `username (CharField)` – Unique identifier.
- `email (EmailField)` – Contact information.
- `password (CharField)` – For authentication.
- `role (CharField)` – Either "admin" or "customer."

**Relationships**:
- **One-to-Many**: Each user can have multiple custom orders.

---

#### 2. Custom Order Model (Users App)
Stores details of personalized artwork requests submitted by users.

**Fields**:
- `user (ForeignKey to User)` – Links the order to the user who made it.
- `details (TextField)` – Customization instructions.
- `price (DecimalField)` – Cost of the custom work.
- `status (CharField)` – Tracks progress: "Pending", "In Progress", or "Completed."

**Relationships**:
- **ForeignKey**: Each custom order belongs to one user.

---

#### 3. Artwork Model (Artwork App)
Represents individual artworks for sale.

**Fields**:
- `title (CharField)` – Artwork name.
- `description (TextField)` – Details about the piece.
- `price (DecimalField)` – Selling price.
- `image (ImageField)` – Artwork file upload.
- `artist (ForeignKey to Artist)` – Links to the artist profile.

**Relationships**:
- **ForeignKey**: Each artwork is associated with one artist.

---

#### 4. Artist Model (Core App)
Represents contributing artists and their bios.

**Fields**:
- `name (CharField)` – Artist’s full name.
- `bio (TextField)` – Description or profile.
- `website (URLField)` - Optional portfolio link.

---

#### 5. Order Model (Orders App)
Handles shopping cart and purchases.

**Fields**:
- `user (ForeignKey to User)` – Connects the order to the buyer.
- `artwork (ManyToManyField to Artwork)` – Stores multiple items in the order.
- `status (CharField)` – Payment status: "Pending" or "Completed."

**Relationships**:
- **Many-to-Many**: A single order can include multiple artworks

---

## Testing

### 1. Manual Testing
| Feature          | Test Case                     | Status    |
|------------------|-------------------------------|-----------|
| Navbar Links     | Ensure all links navigate correctly | ✅ Passed |
| Delivery Details | Save delivery info to order   | ✅ Passed |
| Payment Processing | Verify Stripe integration   | ✅ Passed |

### 2. BDD testing with user stories: 
### User Stories and BDD Scenarios

#### **User Story 2: Viewing Artwork Details**
**As a customer,**  
I want to click on an artwork to see more details, including artist information and pricing.  

**Acceptance Criteria:**  
1) Clicking on an artwork should open a detail page.  
2) The detail page should display a high-quality image of the artwork.  
3) The artist’s name and biography should be accessible.  

**BDD Scenarios:**  
- **Scenario 1:**  
  *Given* the user is on the Shop page,  
  *When* they click on an artwork,  
  *Then* they should be redirected to the artwork’s detail page.  

- **Scenario 2:**  
  *Given* the user is on an artwork’s detail page,  
  *When* they view the image section,  
  *Then* they should see a high-resolution image of the artwork.  

- **Scenario 3:**  
  *Given* the user is on an artwork’s detail page,  
  *When* they scroll to the artist section,  
  *Then* they should see the artist’s name and biography.  

---

#### **User Story 3: Adding Items to Cart**
**As a customer,**  
I want to add artwork to my shopping cart so that I can review my selections before checkout.  

**Acceptance Criteria:**  
1) The user should see an "Add to Cart" button on artwork pages.  
2) The user should be able to remove items from the cart.  

**BDD Scenarios:**  
- **Scenario 1:**  
  *Given* the user is on the artwork detail page,  
  *When* they click the "Add to Cart" button,  
  *Then* the artwork should be added to their cart.  

- **Scenario 2:**  
  *Given* the user has items in their cart,  
  *When* they click the "Remove" button next to an artwork,  
  *Then* the artwork should be removed from the cart.  

---

#### **User Story 4: Checking Out & Making Payments**
**As a customer,**  
I want to securely pay for my order so that I can receive my purchased artwork.  

**Acceptance Criteria:**  
1) The user should be able to review items before checkout.  
2) The checkout page should display a breakdown of costs.  
3) Payment options should include secure processing via Stripe.  
4) The user should receive confirmation upon a successful transaction.  

**BDD Scenarios:**  
- **Scenario 1:**  
  *Given* the user has items in their cart,  
  *When* they navigate to the checkout page,  
  *Then* they should see a list of all selected items.  

- **Scenario 2:**  
  *Given* the user is on the checkout page,  
  *When* they review the summary section,  
  *Then* they should see a breakdown of item costs, tax, and total.  

- **Scenario 3:**  
  *Given* the user is on the checkout page,  
  *When* they enter their payment details,  
  *Then* the payment should be securely processed.  

- **Scenario 4:**  
  *Given* the user has successfully paid,  
  *When* the payment is confirmed,  
  *Then* they should receive a confirmation message.  

---

#### **User Story 5: Requesting Custom Artwork**
**As a customer,**  
I want to submit a request for custom artwork so that I can purchase personalized pieces.  

**Acceptance Criteria:**  
1) The user should be able to fill out a custom order request form.  
2) The request should be stored for admin review.  
3) Users should receive a confirmation after submission.  

**BDD Scenarios:**  
- **Scenario 1:**  
  *Given* the user is on the custom order page,  
  *When* they fill out the form,  
  *Then* the form should accept all required details.  

- **Scenario 2:**  
  *Given* the user submits the request form,  
  *When* the submission is processed,  
  *Then* the order should be saved in the database.  

- **Scenario 3:**  
  *Given* the user has submitted the form,  
  *When* the system processes the submission,  
  *Then* they should see a confirmation message.  

---

#### **User Story 6: Tracking Order History**
**As a customer,**  
I want to see a history of my orders so that I can review my past purchases.  

**Acceptance Criteria:**  
1) The user should access their order history from the dashboard.  
2) Orders should include artwork details, purchase date, and status.  
3) Users should be able to view the details of each past order.  

**BDD Scenarios:**  
- **Scenario 1:**  
  *Given* the user is logged into their account,  
  *When* they navigate to the dashboard,  
  *Then* they should see a list of their previous orders.  

- **Scenario 2:**  
  *Given* the user is viewing their order history,  
  *When* they review the order list,  
  *Then* each order should show artwork details, purchase date, and status.  

- **Scenario 3:**  
  *Given* the user clicks on a specific order,  
  *When* the order details page loads,  
  *Then* they should see a detailed view of that order.  

---

#### **User Story 7: Searching for Artwork**
**As a user,**  
I want to search for artwork using keywords so that I can find specific pieces quickly.  

**Acceptance Criteria:**  
1) The user should see a search bar on the Shop page and homepage.  
2) Users can type keywords related to artwork titles or artist names.  
3) The search results should display matching artworks dynamically.  
4) If no matching artwork is found, an appropriate message should be shown.  

**BDD Scenarios:**  
- **Scenario: Searching for existing artwork**  
  *Given* the user is on the Shop page,  
  *When* they enter a valid artwork title in the search bar,  
  *Then* the results should display artworks matching the keyword.  

- **Scenario: Searching for an artist’s name**  
  *Given* the user is on the Shop page,  
  *When* they enter an artist’s name in the search bar,  
  *Then* the results should display all artwork associated with that artist.  

- **Scenario: No results found**  
  *Given* the user is on the Shop page,  
  *When* they enter a keyword that does not match any artwork or artist,  
  *Then* the system should display a "No results found" message.  

### 3. Validator Testing
- HTML, CSS validation using W3C validators.
- Python code validated with PEP8 standards.
- Lighthouse
PEP8
![PEP8](static\images\pep8.png)
CSS
![CSS](static\images\css.png)
Lighthouse
![lighthouse](static\images\lighthouse.png)
---

## Bugs
- **Resolved:** Navbar alignment issue, delivery details not saving correctly.
- **Unresolved:** 

---

## Deployment
- This project was deployed locally first and then hosted on Heroku. Follow these steps to set up and deploy the project: [Deployment file](deployment.md)

---

## Future Enhancements
- Introduce framed print options.
- Add international shipping functionality.
- Enhance artwork customization with live previews.
- Implement advanced analytics to track user behavior.
- and a watermark on images before buying. 

---

## Summary
DreamScapes is the result of a rewarding yet challenging journey, where technical precision met artistic expression to create a unique e-commerce platform. The project was shaped by tight time constraints and unforeseen hurdles, demanding creative problem-solving and adaptability throughout the process.
Time Limitations:
Delivering a functional platform within a set timeframe required prioritizing essential features while scaling back or postponing certain enhancements. This approach ensured the project remained focused and achievable without compromising on user experience or core functionality.
Overcoming Challenges:
- Building DreamScapes involved tackling complex technical challenges:
- Payment Integration: Stripe required meticulous debugging to guarantee secure and seamless transactions.
- Responsive Design: Bootstrap styling necessitated iterative refinements to achieve consistent spacing and responsiveness.
- Custom Artwork Functionality: Designing and implementing forms demanded careful database structuring and troubleshooting.

Despite these obstacles, solutions often involved creative compromises, such as simplifying workflows, streamlining operations, and embracing innovative tools.
Lessons Learned:
The challenges faced during the project were opportunities for growth and skill enhancement. Learning to work within limitations fostered resourcefulness and efficiency, while tackling technical issues improved problem-solving skills and confidence.
DreamScapes stands as a testament to the power of perseverance and passion. It not only serves as a platform for showcasing dream-like artwork but also reflects the dedication and creativity poured into its development. With future enhancements on the horizon, DreamScapes is ready to continue evolving and inspiring art lovers everywhere.

---
## Content
- This project was designed and developed by **Monica Thomas** as part of the Code Institute Full-Stack Development Diploma.

## Credits
DreamScapes was developed with the support of various tools, frameworks, and documentation that guided the implementation of essential features. Special thanks to the following resources:
- Bootstrap Documentation: For providing detailed guidance on implementing responsive design and cohesive styling across the platform.
- Stripe Documentation: For comprehensive instructions on integrating secure payment processing seamlessly into the checkout workflow.
- Cloudinary Documentation: For facilitating efficient media storage and management, ensuring high-quality images are served throughout the site.
- Tech With Tim: [Django Beginner Tutorial](https://youtu.be/sm1mokevMWk?si=x647nUCIvSpyD2lU)
- Programming with Mosh: [Django Full Course](https://youtu.be/rHux0gMZ3Eg?si=SBKdrSZ061fcF1YV)  

Additionally, the Django framework and its community resources played a crucial role in building the backend logic and overall structure of the platform. Tutorials, blogs, and mentors also provided valuable insights along the way.


## Acknowledgements
- Special thanks to the Code Institute community and my mentor Iuliia Konovalova for support and guidance throughout this project.