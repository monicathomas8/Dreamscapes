### User Model (`users` app)

| Field       | Type        | Description                | Relationship              |
|-------------|-------------|----------------------------|---------------------------|
| username    | CharField   | Unique user identifier     | -                         |
| email       | EmailField  | User’s email address       | -                         |
| password    | CharField   | Hashed password            | -                         |
| first_name  | CharField   | First name                 | -                         |
| last_name   | CharField   | Last name                  | -                         |
| is_artist   | BooleanField| Optional flag for artist role | Links to Artist bio   |

### CustomOrder Model (`users` app)

| Field             | Type         | Description                        | Relationship     |
|------------------|--------------|------------------------------------|------------------|
| user             | ForeignKey   | Associated user                    | FK to User       |
| description      | TextField    | Custom request description         | -                |
| size             | CharField    | Requested size (e.g. A4)           | -                |
| colours          | CharField    | Preferred colours                  | -                |
| theme            | CharField    | Thematic concept                   | -                |
| style            | CharField    | Style like "minimalist", "abstract" | -               |
| extra_suggestions| TextField    | Any additional notes               | -                |
| contact_email    | EmailField   | For communication                  | -                |
| status           | CharField    | Pending/In Progress/Completed      | -                |
| created_at       | DateTimeField| Time of submission                 | -                |

### Artwork Model (`artworks` app)

| Field       | Type         | Description                | Relationship |
|-------------|--------------|----------------------------|--------------|
| title       | CharField    | Artwork title              | -            |
| description | TextField    | Artwork details            | -            |
| price       | DecimalField | Price in GBP               | -            |
| image       | ImageField   | Uploaded image             | -            |
| theme       | CharField    | Theme (e.g. night, ocean)  | -            |
| style       | CharField    | Artistic style             | -            |
| keywords    | CharField    | For search filtering       | -            |

### Artist Bio Model (optional)

| Field    | Type          | Description            | Relationship      |
|----------|---------------|------------------------|-------------------|
| user     | OneToOneField | Connected user profile | 1:1 with User     |
| bio      | TextField     | Artist biography       | -                 |
| website  | URLField      | External portfolio link| -                 |

### Order Model (`orders` app)

| Field           | Type           | Description              | Relationship     |
|----------------|----------------|--------------------------|------------------|
| user           | ForeignKey     | Buyer                    | FK to User       |
| items          | ManyToManyField| Artworks in the order    | M2M with Artwork |
| total_price    | DecimalField   | Combined cost            | -                |
| status         | CharField      | Pending / Completed      | -                |
| created_at     | DateTimeField  | Order timestamp          | -                |
| first_name     | CharField      | Customer first name      | -                |
| last_name      | CharField      | Customer last name       | -                |
| email          | EmailField     | Email for confirmation   | -                |
| address_line_1 | CharField      | Shipping address         | -                |
| address_line_2 | CharField      | Optional second line     | -                |
| city           | CharField      | City                     | -                |
| postal_code    | CharField      | ZIP/Postcode             | -                |
| country        | CharField      | UK only (currently)      | -                |