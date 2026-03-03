# Theme Modifications

To implement the Services and Issues pages with wide 2-column grids and custom buttons, the following modifications were made to the original Tailbliss Hugo theme:

## 1. Custom Page Layout (`layouts/page/wide.html`)
The default Hugo theme layout (`layouts/_default/single.html`) wraps all markdown content in a `prose` Tailwind class, which strictly limits the maximum width of the text container to roughly 65 characters to optimize for reading long blog posts. This caused our 2-column grid and button links to be squished together, forcing text to wrap awkwardly.

**Fix:** 
Created a new layout file at `layouts/page/wide.html` that removed the `prose` class and replaced it with a wider max-width constraint (`max-w-5xl`).
This allows any markdown page using `type: "page"` and `layout: "wide"` in its front matter to spread out and utilize the full space of the screen, providing room for our wide service grids.

## 2. Navigation Menu (`hugo.yaml`)
The original theme included several non-functional dummy dropdown links in the main top navigation bar.

**Fix:**
Updated the `menu.main` array in the `hugo.yaml` configuration file. Removed the dummy dropdowns (appearance/comments/analytics), and explicitly defined straightforward links to:
- Services (`/services/`)
- Issues (`/issues/`)
- About (`/about/`)
- Contact (`/contact/`)

## 3. Local Icons (`static/images/icons/`)
Rather than assigning FontAwesome classes or relying on the SimpleIcons CDN inside the theme imagery, we downloaded all of the official SVG vector logos and placed them directly inside the Hugo static assets directory (`/static/images/icons/`). This theme modification guarantees the site renders flawlessly even if the Unraid instance is moved to a completely disconnected or offline network.
