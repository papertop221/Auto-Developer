# Tech Stack Guidelines for Auto Developer

## Professional Scaffolding (Web)
**Default Structure**:
- `/src/components/ui`: Primitive UI components (shadcn style).
- `/src/lib`: Shared utilities, API clients, and database clients.
- `/src/hooks`: Custom React hooks for logic reuse.
- `/src/types`: Centralized TypeScript definitions.
- `/.env.example`: Template for environment variables (NEVER commit `.env`).

## Implementation Rules:
- **Security**: Use `Zod` or similar for runtime schema validation.
- **State**: Prefer server components for data fetching; use `Zustand` or context for global client state if needed.
- **Icons**: Standardize on `lucide-react`.

## Professional Scaffolding (Python)
**Default Structure**:
- `/src`: Main application logic.
- `/tests`: Comprehensive test suite.
- `main.py`: Entry point.
- `conftest.py`: Shared test fixtures.

