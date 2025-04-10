## CODING


examples = """
Input: [150000, 180000, 200000, 170000] -> Output: 175000.0
Input: [10000, 25000, 30000, 15000] -> Output: 20000.0
Input: [50000, 75000, 60000, 45000] -> Output: 57500.0
"""

def calculate_average_sales(quarterly_sales):
    """
    Calculate the average of quarterly sales data.
    
    Args:
        quarterly_sales (list): List of sales figures for each quarter
        
    Returns:
        float: Average sales across all quarters
    """
    if not quarterly_sales:
        return 0.0
    
    return sum(quarterly_sales) / len(quarterly_sales)

# Test cases based on examples
test_cases = [
    [150000, 180000, 200000, 170000],
    [10000, 25000, 30000, 15000],
    [50000, 75000, 60000, 45000]
]

for sales_data in test_cases:
    result = calculate_average_sales(sales_data)
    print(f"Input: {sales_data} -> Output: {result}")


## SUMMARIZING BUSINESS REPORTS

# 1
prompt = f"""
summarizes the report (formatted using f-string) in maximum five sentences, while focusing on aspects related to AI and data privacy {report}.
"""


# 2
product_description = """
\nThe Smartphone XYZ-5000 is a device packed with innovative features to enhance the user experience. Its sleek design and vibrant display make it visually appealing, while the powerful octa-core processor ensures smooth performance and multitasking capabilities.\nThe XYZ-5000 boasts a high-resolution triple-camera system, combining a 48MP primary lens, a 12MP ultra-wide lens, and a 5MP depth sensor, enabling users to capture stunning photos and videos in various shooting scenarios. The device also supports 4K video recording and comes with advanced image stabilization features.\nWith a generous 128GB of internal storage, expandable up to 512GB via microSD, users can store a vast collection of media files and apps without worrying about running out of space. The smartphone runs on the latest Android OS and offers seamless integration with various Google services.\nIn terms of security, the XYZ-5000 features a reliable fingerprint sensor and facial recognition technology for quick and secure unlocking. Additionally, it supports NFC for contactless payments and has a dedicated AI-powered virtual assistant to simplify daily tasks.\nThe device's long-lasting 4000mAh battery ensures all-day usage, and it supports fast charging, providing hours of power with just a few minutes of charging. The XYZ-5000 is also water and dust resistant, giving users peace of mind in various environments.\nOverall, the Smartphone XYZ-5000 offers a fantastic combination of style, performance, and advanced features, making it an excellent choice for tech enthusiasts and everyday users alike.\n
"""


prompt = f"""
Summarizes the product description in no more than five bullet points.
Product_description is given between three backticks ```{product_description}```
"""


# 3


product_description = """'\nProduct: "Smart Home Security Camera"\n- High-tech security camera with night vision and motion detection.\n- Easy setup and remote monitoring.\n- Two-way audio communication for real-time interaction.\n- Mobile app integration for convenient control and alerts.\n- Weather-resistant design for both indoor and outdoor use.\n- Smart AI algorithms for advanced person and object detection.\n- Cloud storage and local backup options for recorded footage.\n- Infrared LEDs for clear imaging even in complete darkness.\n- Customizable motion zones to focus on specific areas.\n- Compatibility with voice assistants for hands-free control.\n'"""

prompt = f"""
Expand the product description pre-loaded string, and write a one paragraph comprehensive overview capturing the key information of the product: unique features, benefits, and potential applications.
Product description is given between three backticks ```{product_description}```.
"""
