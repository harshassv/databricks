#### Team: Up!
Team member - 1 : AKHIL SONGA

Email Address : as5735@drexel.edu (professional), akhilsonga1@gmail.com (personal)

Organization : DREXEL UNIVERSITY

Country : USA

Team member - 2: NAGA VENKATA SURYA SAI TANMAI RAAVI

Email Address : nr638@drexel.edu (professional), saitanmai.raavi@gmail.com (personal)

Organization : DREXEL UNIVERSITY

Country : USA

Team Member - 3: SAI VASAVI HARSHAVARDHAN GUPTA SOMISETTY

Email Address : ss5536@drexel.edu (professional), harshassv.13@gmail.com (personal)

Organization : DREXEL UNIVERSITY

Country : USA

#####Industry prize or Prize category: 

**Retail and Consumer Goods (RCG)**

## Inspiration

Up! was inspired by the untapped potential of underprivileged entrepreneurs, driven by a vision to democratize AI. Witnessing their resilience and determination, we aimed to break down barriers to innovation. Our inspiration? Empowering small businesses to thrive in a digital era, regardless of resources or expertise. Up! is more than just a tool—it's a beacon of opportunity and a catalyst for success. Join us in revolutionizing the way underprivileged entrepreneurs interact with technology, no code AI for better customer support and operations for business.

## What it does

**The Up! app offers boundless possibilities to sellers, limited only by their imagination. Here are some of its standout features:**

i. Sellers can effortlessly create customized bots by simply filling out a Google form. This streamlines various processes within the organization. From crafting order bots to facilitate seamless checkout experiences for customers, to developing customer service bots and beyond, the potential is endless.

ii. Leveraging webhooks extensively, the Up! app provides sellers with a unified view across all their different accounts. This creates an omni-channel experience for customers, granting them the flexibility to interact both online and in-person. The Up! app seamlessly delivers the right data to the right entity, ensuring convenience and efficiency.

iii. We've engineered seven custom-made agents for sellers, enhancing both customer experiences and operational efficiency.

iv. With natural language capabilities, sellers can effortlessly create automated workflows. For instance, if a new item is added to the inventory, a simple query like, "Can you send emails to all customers who may be interested in the newly added products?" triggers the Up! app to handle the task seamlessly.

v. Sellers can easily stay abreast of the latest trends and competition using the Up! app's report analyst and web surfer functionalities. This ensures they remain competitive in the market, preventing customers from seeking products elsewhere.

vi. Through the inventory manager, sellers gain extensive control over their inventory, ensuring they always have the right amount of stock to satisfy customer demands.

These are just a few examples of how sellers can harness the power of AI through the seven agents provided by the Up! app, ultimately enhancing the customer journey and driving business success.

## How we built it

Our product is designed for small to medium businesses, utilizes a vast number of custom-built Python agents combined to form multiple assistants tailored to emulate an entrepreneurial assistant. Powered by a DBRX. Streamlit for UI.

Under the surface,**a team of 28 agents** operates seamlessly to support these assistants. These include Python agents, prompt agents, communicators, report generators, internet browsers, quality control monitors, memory processors, prompt improvisers, schedulers  and more. Our approach draws from the ReAct research paper link for agile and effective task execution.

API Selection: Based on our requirements, we chose specific APIs from Square that aligned with our project goals, including the Catalog API, Inventory API, Webhooks, and Customer API. These APIs formed the foundation for our AI-powered platform, enabling seamless integration with Square's services.

AI Integration: We integrated AI capabilities into our platform to enable natural language interaction for business owners. Leveraging NLP algorithms, we developed an AI assistant that understands and responds to user queries and commands in conversational language. This AI assistant serves as the interface between the business owner and the Square APIs, facilitating intuitive interaction and task execution.

Catalog API Integration: With AI-driven interaction, business owners can use natural language to manage their product catalog through the Catalog API. The AI assistant interprets commands such as "Add a new item" or "Update product details" and communicates with the Catalog API to perform the corresponding actions seamlessly.

Inventory API Integration: Utilizing AI-driven capabilities, business owners can manage inventory effortlessly using natural language commands. For example, they can ask the AI assistant to "Check stock levels" or "Notify me when inventory is low," triggering interactions with the Inventory API to provide real-time updates and alerts.

Webhooks Implementation: The AI assistant continuously monitors events and updates from Square using Webhooks, allowing for proactive notifications and responses to relevant activities. For instance, when a new order is received, the AI assistant can notify the business owner and provide options for order fulfillment, all through natural language interaction.

Customer API Integration: Through AI-driven communication, business owners can engage with customer data and activities using conversational language. The AI assistant can retrieve customer information, track purchase history, and personalize interactions based on individual preferences, leveraging the capabilities of the Customer API to enhance customer engagement.

Testing and Optimization: Throughout the development process, we conducted rigorous testing to ensure the accuracy, reliability, and responsiveness of the AI assistant and its integration with Square APIs. We iteratively optimized the NLP algorithms and AI models to improve understanding and enhance user experience.

**For example we have the following sub agents that supports the functionality of the main agents:**

i. prompt police

ii. Actions generator agent

iii. Editor agent

iv. Tools scheduler

v. Web surfing agent

vi. Python code generator

vii. Python code checker

viii. Python code error fixer

**and Many More. 
All the agents are made from scratch for this use case.**


## Challenges we ran into

Building all the necessary agents posed a significant challenge, exacerbated by the complexity of facilitating communication between them. Additionally, integrating and optimizing tools for these agents proved time-consuming, like Task Scheduler, Python code executor, Report Generator, etc.

Our core aim is to offer small business owners a straightforward solution without relying on complex methodologies, enabling them to improve operations and ensuring their customers have an excellent experience by harnessing the power of AI.

**We acknowledge the inverse relationship between user-end simplicity and developer-end complexity.**

By employing advanced techniques such as complex regex, data retrieval, and intelligent agent collaboration, we have achieved seamless functionality.

## Accomplishments that we're proud of
Home-grown agents without any frameworks: Our development team has achieved a remarkable feat by creating home-grown AI agents without relying on external frameworks, thus ensuring a seamless and tailored customer experience. This demonstrates our commitment to innovation and our confidence in our team's expertise. By building agents from scratch, we have full control over their functionality, allowing us to enhance the overall customer experience and meet the unique needs of our users.

Robust Inventory Manager: We take pride in the creation of our robust inventory manager, which serves as a cornerstone of our platform, enhancing customer experience by providing efficient and reliable inventory management solutions. Its reliability and effectiveness empower entrepreneurs to streamline their operations, resulting in smoother transactions and happier customers. With our inventory manager, businesses can ensure products are always in stock, leading to increased customer satisfaction and loyalty.

One-stop report generation feature: Our platform offers a seamless solution for generating detailed PDF reports tailored for industry analysis, improving customer experience by providing easy access to crucial insights. With just a few clicks, users can access a comprehensive array of data insights, trends, and performance metrics, compiled into professionally formatted reports. This streamlined approach saves valuable time and resources, allowing businesses to focus on delivering exceptional customer experiences and staying ahead of the competition.

Most Proud of: We have successfully integrated our platform with Square, expanding its functionality and usability, ultimately enhancing the customer experience. By integrating with Square, we offer businesses a seamless payment processing solution, providing customers with a convenient and secure payment experience. This integration enhances the versatility and value of our platform, catering to diverse business needs and preferences while ensuring a positive customer experience at every touch point.
## What we learned
How to make custom agents and tailored tools that work together in order to ease the business owner. And we learned how to use the fantastic framework of Square and their initiatives to help small community sellers. And I'm very happy to be a part of this, and to be part of that help. By developing this app we were able to learn how to use Databricks and it's importance. 

## What's next for Up!
Firstly, we plan to introduce a personalized bot that can joins  Zoom meetings with business owners to discuss their specific needs and challenges. This bot will facilitate direct communication, allowing for more in-depth conversations and tailored solutions. By leveraging Zoom, we aim to provide a convenient and interactive platform for business owners to engage with AI and explore how its recommendations can optimize their operations.

Additionally, we recognize the importance of accessibility and simplicity for business owners who may not be tech-savvy. To address this, we envision creating bots that can assist with tasks such as inventory management, appointment scheduling, and customer inquiries. Business owners can simply call the bot and provide instructions or queries, and the bot will execute the tasks or provide relevant information in real-time. This streamlined approach eliminates the need for complex interfaces or technical know-how, making it easier for business owners to manage their operations on the go.

**[Up! documentation page](https://harshavardhans-organization.gitbook.io/up/)**
