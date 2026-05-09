# Infrastructure & Automatic Cloud Provisioning

`auto-developer` ensures the project is not just built, but deployed and scalable.

## 1. Containerization
- **Dockerfile**: Create optimized, multi-stage Dockerfiles for the project stack.
- **Docker Compose**: Include a `docker-compose.yml` for local development (including databases and caches).

## 2. Infrastructure as Code (IaC)
- Generate configuration for popular platforms:
    - **Vercel/Netlify**: `vercel.json` or `netlify.toml`.
    - **Railway/Render**: `railway.json` or `render.yaml`.
    - **Terraform/Pulumi**: Basic cloud provisioning scripts for AWS/GCP/Azure if requested.

## 3. Continuous Integration (CI/CD)
- **GitHub Actions**: Automate testing and deployment on every push.
- **Health Checks**: Implement `/api/health` endpoints to monitor application uptime.

## 4. One-Click Launch
- Provide the user with a single `DEPLOY.md` containing the commands to push the project live.
