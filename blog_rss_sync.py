import feedparser
from datetime import datetime

URL = "https://mertsismanoglu.com/rss"
README = "README.md"
MARKER = "<!-- BLOG-POST-LIST -->"

def fetch_posts():
    """Fetch all posts from RSS feed (duplicate checking happens in update_readme)."""
    feed = feedparser.parse(URL)
    posts = []
    for entry in feed.entries:
        posts.append(f"- [{entry.title}]({entry.link})")
    return posts

def get_existing_posts(content):
    """Extract existing blog post URLs from README content."""
    before, marker, after = content.partition(MARKER)
    if not marker:
        return set()
    
    # Find the end of the blog post list
    end_marker_pos = after.find("<!-- ")
    if end_marker_pos == -1:
        # If no end marker, look for the next section (##)
        end_marker_pos = after.find("\n##")
    
    if end_marker_pos == -1:
        blog_section = after
    else:
        blog_section = after[:end_marker_pos]
    
    # Extract URLs from markdown links
    existing_urls = set()
    lines = blog_section.strip().split('\n')
    for line in lines:
        if line.startswith('- [') and '](' in line:
            start = line.find('](') + 2
            end = line.find(')', start)
            if start > 1 and end > start:
                existing_urls.add(line[start:end])
    
    return existing_urls

def update_readme():
    with open(README, "r", encoding="utf-8") as f:
        content = f.read()

    before, marker, after = content.partition(MARKER)
    if marker:
        # Get existing post URLs to avoid duplicates
        existing_urls = get_existing_posts(content)
        
        # Filter out duplicate posts
        feed = feedparser.parse(URL)
        new_posts = []
        for entry in feed.entries:
            if entry.link not in existing_urls:
                new_posts.append(f"- [{entry.title}]({entry.link})")
            if len(new_posts) >= 5:  # Limit to 5 new posts
                break
        
        if new_posts:
            # Get existing posts from content for merging
            end_marker_pos = after.find("<!-- ")
            if end_marker_pos == -1:
                end_marker_pos = after.find("\n##")
            
            if end_marker_pos == -1:
                existing_blog_content = after.strip()
                remaining_content = ""
            else:
                existing_blog_content = after[:end_marker_pos].strip()
                remaining_content = after[end_marker_pos:]
            
            # Combine new posts with existing ones, limit total to 5
            all_posts = new_posts[:]
            if existing_blog_content:
                existing_lines = [line for line in existing_blog_content.split('\n') if line.startswith('- [')]
                all_posts.extend(existing_lines)
            
            # Keep only the latest 5 posts
            final_posts = all_posts[:5]
            
            new_content = f"{before}{marker}\n{chr(10).join(final_posts)}\n{remaining_content}"
        else:
            # No new posts, keep existing content
            new_content = content
            
        with open(README, "w", encoding="utf-8") as f:
            f.write(new_content)

if __name__ == "__main__":
    update_readme()
