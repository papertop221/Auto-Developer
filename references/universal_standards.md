# Global Accessibility & Internationalization (i18n) Standards

To ensure `auto-developer` creates software that benefits the entire world, all projects must adhere to these universal standards.

## 1. Internationalization (i18n)
Every application must be built to support multiple languages and locales.
- **Rule**: Never hardcode user-facing strings. Use a localization library (e.g., `next-intl` for Web, `gettext` for Python).
- **Structure**: Maintain a `/messages` or `/locales` directory containing JSON translation files (e.g., `en.json`, `es.json`).
- **Directionality**: Ensure UI layouts support Right-to-Left (RTL) languages like Arabic or Hebrew if requested.

## 2. Accessibility (a11y)
Software must be usable by people with disabilities (WCAG 2.1 Compliance).
- **Semantic HTML**: Use proper tags (`<main>`, `<nav>`, `<button>`) instead of generic `<div>` tags.
- **ARIA Attributes**: Include `aria-label`, `aria-hidden`, and `role` attributes where necessary for screen readers.
- **Keyboard Navigation**: Ensure all interactive elements are focusable and navigable via the Tab key.
- **Contrast**: Maintain a minimum contrast ratio of 4.5:1 for text.

## 3. Privacy & Compliance (Global Laws)
- **GDPR/CCPA Readiness**: Include a standard "Cookie Consent" and "Privacy Policy" template.
- **Data Portability**: Implement basic logic for users to export or delete their personal data.
- **Security**: Use HTTPS-only headers and secure cookie configurations by default.

## 4. Universal Time & Units
- **Timezones**: Always store timestamps in UTC and convert to the user's local timezone only at the UI layer.
- **Formatting**: Use the user's locale for date, currency, and number formatting.
