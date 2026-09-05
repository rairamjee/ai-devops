# AI for DevOps

## 1. Project Overview

AI for DevOps is a practical, structured learning platform designed to teach modern DevOps from fundamentals through advanced, production-oriented practices, with AI integrated throughout the learning experience.

The goal is not to create a collection of documentation pages. The goal is to build an interactive learning website where a learner can understand concepts, see practical examples, complete exercises, build projects, and progressively develop real DevOps skills.

---

## 2. Primary Goals

The platform should:

- Teach DevOps from beginner to advanced level.
- Explain concepts clearly rather than simply listing topics.
- Follow a logical learning progression.
- Provide practical examples and commands.
- Include hands-on exercises.
- Include real-world projects.
- Connect concepts to production scenarios.
- Explain why a technology or practice is used.
- Include common mistakes and troubleshooting.
- Integrate AI into the learning experience.
- Track learner progress.
- Make the content easy to navigate and search.
- Keep the content maintainable and modular.

---

## 3. Learning Philosophy

Every major topic should answer:

1. What is it?
2. Why does it exist?
3. What problem does it solve?
4. How does it work?
5. When should I use it?
6. When should I NOT use it?
7. How is it used in real systems?
8. What can go wrong?
9. How do I troubleshoot it?
10. How does it connect to other DevOps concepts?

Avoid shallow "definition-only" documentation.

The learner should understand the concept well enough to use it in a real environment.

---

## 4. Learning Path

The learning path is organized into folders/modules.

Initial structure:

```text
00-foundations
01-linux
02-networking
03-git
04-containers
05-kubernetes
06-ci-cd
07-cloud
08-reliability
09-observability
10-security
11-infrastructure-as-code
12-ai-for-devops
```

This structure can evolve as the project develops.

---

## 5. Foundations

The `00-foundations` module establishes the mental models required for the rest of the learning path.

It should cover topics such as:

- What is DevOps?
- Software delivery lifecycle
- Development vs operations
- Infrastructure
- Servers
- Applications
- Processes
- Networking fundamentals
- APIs
- Databases
- Environments
- Development/staging/production
- Configuration
- Automation
- Version control
- CI/CD concepts
- Infrastructure as Code
- Containers
- Cloud fundamentals
- Observability
- Reliability
- Security
- DevOps culture

The goal is to build understanding, not just vocabulary.

---

## 6. Content Structure

Each major topic should preferably follow a consistent structure.

Example:

# Topic

## What is it?

Clear explanation.

## Why does it matter?

Explain the practical problem it solves.

## Mental Model

Explain how to think about the concept.

## How It Works

Technical explanation.

## Example

A practical example.

## Hands-on

An exercise the learner can perform.

## Real-World Scenario

Show how the concept appears in production.

## Common Mistakes

Things beginners commonly get wrong.

## Troubleshooting

Typical failures and how to diagnose them.

## Interview Questions

Important questions with explanations.

## Further Exploration

Links or related concepts.

---

## 7. Website

The website should be a real application rather than a simple static documentation dump.

The website should eventually provide:

- Landing page
- Learning-path navigation
- Module pages
- Topic pages
- Search
- Progress tracking
- Interactive examples
- Code blocks
- Terminal-style examples
- Exercises
- Quizzes
- Projects
- AI-assisted explanations
- Related-topic navigation
- Responsive design
- Dark/light theme support

Technology choices should prioritize:

- Maintainability
- Developer experience
- Performance
- Accessibility
- Simplicity
- Extensibility

Do not introduce unnecessary technologies.

---

## 8. AI Features

AI should be integrated where it genuinely improves learning.

Potential capabilities:

- Explain a concept at different difficulty levels.
- Explain errors.
- Help troubleshoot commands.
- Generate practice questions.
- Provide hints without immediately revealing answers.
- Review learner solutions.
- Explain Kubernetes/Docker/Terraform errors.
- Create scenario-based exercises.
- Act as a DevOps mentor.
- Help learners understand logs and incidents.

AI should supplement learning, not replace understanding.

---

## 9. Practical Learning

The platform should progressively move from:

Concept
→ Example
→ Exercise
→ Guided project
→ Real-world scenario
→ Production considerations

Projects should become progressively more complex.

Example progression:

- Run an application locally.
- Containerize it.
- Add CI.
- Deploy it.
- Add infrastructure as code.
- Add observability.
- Add reliability mechanisms.
- Add security controls.
- Introduce failure scenarios.
- Diagnose and recover from incidents.

---

## 10. Reliability

Reliability is a core part of the curriculum.

Topics should include:

- Timeouts
- Retries
- Backoff
- Rate limiting
- Fallbacks
- Circuit breakers
- Health checks
- Graceful degradation
- Load balancing
- Redundancy
- Failure domains
- Capacity
- SLOs
- SLIs
- SLAs
- Error budgets
- Incident response

The emphasis should be on understanding why these mechanisms exist and how they interact.

---

## 11. Code and Examples

Code examples should be:

- Correct
- Minimal where possible
- Runnable when practical
- Explained
- Consistent with the surrounding lesson

Avoid unnecessarily complicated examples.

Commands should explain:

- What the command does
- Why it is being used
- Important flags
- Expected output where useful
- Common errors

Never encourage learners to blindly copy commands.

---

## 12. Content Quality Rules

Content should be:

- Technically accurate
- Practical
- Clear
- Progressive
- Beginner-friendly without being simplistic
- Production-aware
- Consistent in terminology

Avoid:

- Excessive jargon
- Generic AI-generated filler
- Repeating the same explanation
- Huge walls of text
- Tutorials that provide commands without explaining them
- Overengineering simple examples

---

## 13. Repository Organization

Prefer a clear separation between:

- Website/application code
- Learning content
- Configuration
- Exercises
- Projects
- Assets

Do not mix unrelated concerns.

Suggested high-level structure:

```text
ai-for-devops/
├── PROJECT.md
├── README.md
├── website/
├── 00-foundations/
├── 01-linux/
├── 02-networking/
├── 03-git/
├── 04-containers/
├── 05-kubernetes/
├── 06-ci-cd/
├── 07-cloud/
├── 08-reliability/
├── 09-observability/
├── 10-security/
├── 11-infrastructure-as-code/
└── 12-ai-for-devops/
```

The exact structure may be adjusted as the implementation evolves.

---

## 14. Development Principles

When modifying the repository:

1. Inspect existing code before making changes.
2. Do not delete working functionality without a clear reason.
3. Make small, logical changes.
4. Keep unrelated changes separate.
5. Follow the existing project conventions.
6. Prefer simple solutions.
7. Explain significant architectural decisions.
8. Test changes where practical.
9. Check for broken links/imports/routes.
10. Keep documentation synchronized with implementation.

---

## 15. Git Workflow

Use GitHub as the source of truth for the project.

Changes should ideally be:

- Small
- Understandable
- Reviewable
- Related to one goal

Commit messages should clearly describe the change.

Avoid giant commits containing unrelated changes.

---

## 16. Codex Instructions

When working on this repository, Codex should:

1. Read `PROJECT.md` before making significant changes.
2. Inspect the existing repository before proposing implementation.
3. Preserve existing functionality.
4. Avoid unnecessary dependencies.
5. Follow the architecture already established in the repository.
6. Ask for clarification when a requirement is genuinely ambiguous.
7. Prefer incremental implementation.
8. Run appropriate tests/checks after changes.
9. Report what was changed.
10. Report tests/checks performed.
11. Report any known limitations or follow-up work.

Do not rebuild the entire application when only a small change is requested.

---

## 17. Current Project Status

### Completed

- Initial learning roadmap defined.
- Learning path organized into modules.
- Decision made to build a website rather than rely solely on a documentation framework.
- GitHub repository configured for the project.
- Codex repository access configured.

### In Progress

- Website architecture.
- Repository structure.
- Initial website implementation.
- Foundation learning content.

### Next Major Milestones

1. Establish website architecture.
2. Build the initial landing page.
3. Build learning-path navigation.
4. Implement the `00-foundations` module.
5. Establish reusable lesson components.
6. Add exercises and interactive elements.
7. Continue module-by-module development.
8. Add AI learning features.
9. Add progress tracking.
10. Deploy the website.

---

## 18. Important Rule

This project should evolve incrementally.

Do not attempt to build every module, every feature, and every page at once.

Build the foundation first, validate the architecture, then expand.

The quality of the learning experience is more important than the number of pages.
