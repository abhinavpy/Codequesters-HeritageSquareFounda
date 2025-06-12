Below is a step-by-step guide your teammates can follow to set up a healthy contribution workflow using Git for the parent repository [Codequesters-HeritageSquareFounda](https://github.com/2025-Arizona-Opportunity-Hack-Summer/Codequesters-HeritageSquareFounda). You can share these steps with your team:

---

### 1. **Set Up Your Local Environment**

If you’re a collaborator (i.e., you have push access) or if you’re forking the repo to work on your own copy, follow the appropriate steps:

#### **If You’re a Collaborator (Direct Clone)**

- **Clone the Repository:**  
  ```bash
  git clone https://github.com/2025-Arizona-Opportunity-Hack-Summer/Codequesters-HeritageSquareFounda.git
  ```
- **Navigate into the Project Folder:**  
  ```bash
  cd Codequesters-HeritageSquareFounda
  ```

#### **If You Need to Fork First**

- **Fork the Repository on GitHub:**  
  Use the fork button on the repository page to create a copy in your own GitHub account.

- **Clone Your Fork:**  
  ```bash
  git clone https://github.com/<your-username>/Codequesters-HeritageSquareFounda.git
  cd Codequesters-HeritageSquareFounda
  ```
- **Add the Parent Repository as Upstream:**  
  This keeps your fork in sync with the original repository.
  ```bash
  git remote add upstream https://github.com/2025-Arizona-Opportunity-Hack-Summer/Codequesters-HeritageSquareFounda.git
  ```

---

### 2. **Create a Feature Branch**

Always work on a separate branch from `main` to keep your work isolated.

- **Create and Switch to a New Branch:**  
  Replace `feature/your-feature-name` with a brief description of your work.
  ```bash
  git checkout -b feature/your-feature-name
  ```

---

### 3. **Make Your Changes**

- **Edit Files & Develop Your Feature:**  
  Use your favorite IDE or editor (e.g., VS Code) to make changes.

- **Review Changes:**  
  Use Git status or a Git GUI to check which files you modified.
  ```bash
  git status
  ```

---

### 4. **Commit Your Changes**

- **Stage and Commit Changes:**  
  Use clear commit messages describing your changes:
  ```bash
  git add .
  git commit -m "Implement feature: [brief description]"
  ```

---

### 5. **Synchronize With the Upstream Repository**

Before pushing your branch or when starting a new session, get the latest updates to avoid conflicts.

- **If You’re Working on a Fork:**  
  Fetch and merge changes from the parent repository:
  ```bash
  git fetch upstream
  git checkout main
  git merge upstream/main
  ```
  Then, switch back to your feature branch and rebase (or merge) the latest changes:
  ```bash
  git checkout feature/your-feature-name
  git rebase main
  ```
  *Alternatively, you could merge instead of rebasing if that’s your team’s preferred method:*
  ```bash
  git merge main
  ```

- **If You’re a Direct Collaborator:**  
  Simply pull the latest changes on `main`:
  ```bash
  git checkout main
  git pull origin main
  ```
  Then update your branch:
  ```bash
  git checkout feature/your-feature-name
  git rebase main
  ```

---

### 6. **Push Your Branch to GitHub**

- **Push to Your Fork or the Main Repository (if you’re a collaborator):**  
  ```bash
  git push origin feature/your-feature-name
  ```

---

### 7. **Create a Pull Request (PR)**

- **Open the GitHub Repo in Your Browser:**  
  Navigate to your repository’s page.
  
- **Create a New PR:**  
  You should see a prompt to create a Pull Request for your recently pushed branch. Follow the instructions:
  - Ensure the base branch is set to `main`.
  - Provide a clear title and description detailing the changes you’ve made.
  
- **Request Reviews:**  
  Tag your teammates or assign reviewers so that your changes can be reviewed before merging.

---

### 8. **Collaborative Code Review & Merge**

- **Participate in the Review Process:**  
  Address any suggested changes by your teammates.
  
- **Merge the PR:**  
  Once approved and after resolving any merge conflicts, merge your PR.  
  *If you’re not authorized to merge, a designated team member (or lead) will do it.*

---

### 9. **Clean Up Local Branches**

After your feature branch has been merged into `main`, clean up your local branches:

- **Switch to `main` and Pull the Latest Changes:**
  ```bash
  git checkout main
  git pull origin main
  ```
- **Delete the Merged Branch Locally:**
  ```bash
  git branch -d feature/your-feature-name
  ```

- **If Using a Fork, Delete the Remote Branch:**  
  ```bash
  git push origin --delete feature/your-feature-name
  ```

---

### Additional Tips

- **Commit Message Guidelines:**  
  Follow the team’s conventions for commit messages if available. Clear messages help with tracking history.
  
- **Branch Naming:**  
  Use descriptive names such as `feature/login-form`, `bugfix/header-alignment`, or `chore/dependencies-update` to indicate the nature of your work.

- **Frequent Commits:**  
  Commit your changes in logical, small increments. This makes it easier to track progress and spot issues.

- **Communication:**  
  Use the team Slack channel or project management tools to discuss which feature branches are active, incoming PRs, and any merge conflicts early on.

---

By adhering to these steps, your team will maintain a smooth Git workflow while contributing to the Codequesters-HeritageSquareFounda repository. Feel free to ask if you’d like details on advanced Git topics or integrated workflows with CI/CD.