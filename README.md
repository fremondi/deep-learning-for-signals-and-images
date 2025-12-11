# Coursework - Deep Learning Module 2025
## 100% of Final Module Mark (Read Carefully!)

This repository contains the assessment materials for the ESE MSc Deep Learning course. This coursework is the only assessment 
for the module and accounts for **100% of your final mark**.

| **COURSEWORK** | **Date and time** |
| :------------------ | :---: |
| *Release* | Thursday 11 Dec 14:00h |
| *Due (deadline)* | Friday 12 Dec 18:00h |

The assessment consists of **two questions**, each divided into **Parts A, B, and C**. 
You will find **one Jupyter notebook template per question** inside this repository. All tasks and prompts are contained within these notebooks.

You must complete the tasks *directly in the provided notebooks*.  
Do not rename the files or create additional notebooks.  

**Only the two notebooks will be marked; all other files in the repository will be disregarded.**


# Table of contents

1. [Assessment description](#description)
2. [Deliverables](#deliverables)
3. [Marking Criteria](#criteria)
4. [On Open-Endedness](#open-endedness)
5. [Academic integrity](#academicintegrity)
6. [Hugging Face](#huggingface)
7. [FAQ](#faq)


## Assessment description <a name="description"></a>

For our assessment, we will be exploring two types of very relevant medical data:

1. Magnetic Resonance Imaging (MRI) data, consisting of images acquired with varying protocols to highlight different tissues in the human brain.
2. Electrocardiogram (ECG) data, which records electrical activity in the heart over a certain time period.

AI is taking an increasingly large role in medicine - your role in this assessment is to become, for a few hours, Medical AI scientists
to solve some very real and pressing problems with a potentially high impact on global healthcare.



## Deliverables <a name="deliverables"></a>

You must submit:

1. The completed `Assessment_Q1.ipynb` file - The name of the file should remain unchanged. The file should contain your answers to all assessment questions.
The internal format of the notebook should also remain unchanged, but you are free to add new code and text cells as required to your answers. The notebook's cells
should be executed and saved: we will only mark cells that are executed and will not execute cells for you.

2. The completed `Assessment_Q2.ipynb` file - The name of the file should remain unchanged. The file should contain your answers to all assessment questions.
The internal format of the notebook should also remain unchanged, but you are free to add new code and text cells as required to your answers. The notebook's cells
should be executed and saved: we will only mark cells that are executed and will not execute cells for you.

3. The completed `References.md` file - List in this file your references using the template provided. See the section on *Academic integrity* below.

4. Fill in the [Academic integrity declaration form](https://forms.office.com/e/6McPxhV5Xs) - Please, carefully read, fill, and submit this form in addition to your GitHub Classroom submission. See the section on *Academic integrity* below.


Your final submission must be committed to your GitHub Classroom repository before the deadline. Only your latest commit prior to the 
deadline will be assessed.

**Important:** You must ensure that the uploaded notebooks have all cells run so that all outputs (plots, tables, metrics, images, etc.) are 
clearly visible.  

We reserve the right to rerun your notebooks to ensure that the outputs represent your work accurately. Failure to ensure reproducible 
and truthful outputs may be considered a breach of conduct and may result in disciplinary action.

The deadline for this assessment is:

***December 12th, 2025 at 18:00***

Please ensure:

- all work is committed and pushed before the deadline;  
- you verify that both notebooks render correctly and contain your final solutions;  
- you allow sufficient time for uploads and avoid last-minute technical issues.

**Only your latest submission before the deadline will be marked. We cannot take responsibility for avoidable technical errors or missing work.**



## Marking Criteria <a name="criteria"></a>

Your work will be evaluated based on the following:

### 1. Correctness of model and hyperparameter choices  
Models, architectures, loss functions, and training strategies must be appropriate for the tasks and justified where required.

### 2. Performance and quality of results  
Your models should perform well according to suitable quantitative and/or qualitative criteria relevant to each question.

### 3. Validation strategy  
We will assess the rigour and relevance of your chosen validation procedures, including metrics, plots, diagnostics, and methodological reasoning.

### 4. Complexity of your solution  
More sophisticated methods (for example, transformers, VAEs, or diffusion models) will be credited appropriately when used correctly. Simpler models are acceptable but may receive fewer marks if not well motivated or if they underperform.

You may include **up to two** architecture solutions to each question, noting that you may still be able to obtain marks on the complexity and correctness of the solution even if the model is not fully working or has not produced performing results.

### 5. Creativity of your pipeline  
This includes thoughtful approaches to model design, feature extraction, pre-processing, architecture modification, loss engineering, or other innovations that extend beyond minimal baseline solutions.

### 6. Tidiness and organisation of your notebook  
Your notebooks should be clean, readable, and clearly structured.  
Only include code that is directly relevant to your solution and outputs; remove unused cells, experiments that were abandoned, or redundant intermediate code.  
Excessive clutter, unnecessary outputs, and undocumented code will be penalised.

### 7. Quality and conciseness of written discussion (Parts 1.C and 2.C)  
You must **critically** analyse results from what you have learned in the course. Can you understand the limitations and strengths of your unique implementation to address this specific task?

You must address each prompt directly and adhere to the stated maximum length. Overly long or unfocused discussions will be penalised.



## On Open-Endedness <a name="open-endedness"></a>

The coursework is intentionally open-ended.  

There are many viable correct solutions, and likewise many incorrect ones.  

You should make design choices based on **your** understanding of the lectures, the tasks, and your experimental findings. 
**There are no canonical answers**, and you will be assessed on the quality of your reasoning and implementation.



## Academic Integrity and Authenticity <a name="academicintegrity"></a>

Academic misconduct, including plagiarism, collusion, and inappropriate use of AI tools, is strictly prohibited and may lead to severe disciplinary action.

This is an open-book assessment and you can use resources online. 
However, we expect that you carefully review and understand every aspect of your submission (code, documentation, comments, etc.).
If you use AI tools, you should use them solely for learning, research, or understanding purposes rather than for directly solving assessment tasks.
We expect that all "human-readable" text in the assessment (including documentation, comments, and explanations) are written in your own words, accurately representing your personal understanding, knowledge, and opinions.
We also expect you to undertake this assessment individually and not discuss your answers with other students.

If you use any external sources outside the lecture notes, you should declare these in a `References.md` file and explained their usage in the code through comments and markdown, ensuring full transparency.
Populate the markdown file in the repository called `References.md` with links to sites you have used, papers you have read, links to your chatGPT prompts and answers, and any other resource that you have used to help you design your model.

Expect to be invited to an authenticity to discuss or justify any aspect of your submission, 
and you should be prepared to explain any part of your work in detail if required.

Your commit history will be reviewed; submissions with few or late commits may be flagged.

As part of the assessment, it is **mandatory** that you fill in this [Academic integrity declaration](https://forms.office.com/e/6McPxhV5Xs).
**Assessments without a corresponding declaration will not be marked.**

**You are responsible for ensuring that your submitted work is original and properly developed throughout the coursework period.**



## Hugging Face Token Configuration <a name="huggingface"></a>

We will be using Hugging Face to download the datasets. Instructions to download each dataset are contained within the respective notebooks.

If you encounter authentication issues or rate limiting (e.g. `HTTPError: 429 Client Error: Too Many Requests`) when downloading from Hugging Face, 
you might need to configure an access token. Follow these steps:

1.  **Generate a Hugging Face Token:**
    *   Go to [https://huggingface.co/](https://huggingface.co/).
    * Log in to your account. If you don't have one, you'll need to create one.
    * Navigate to your profile settings by clicking on your avatar (usually in the top right corner) and selecting "Settings".
    * In the left-hand menu, click on "Access Tokens".
    *   Click on "New token", give it a name (e.g., "Colab_Download"), and set the role (usually "read" is sufficient).
    *   Copy the generated token.

2.  **Add the Token to Colab Secrets:**
    *   In Colab, click the "🔑" icon (Secrets) in the left sidebar.
    *   Click "Add new secret".
    *   For "Name", type `HF_TOKEN` (case-sensitive and must be exact).
    *   For "Value", paste your copied Hugging Face token.
    *   Ensure "Notebook access" is enabled.

3.  **Restart Runtime:** After adding the secret, restart your Colab runtime (Runtime > Restart runtime) for the changes to take effect.



## FAQ <a name="faq"></a>

1. **Can I use other deep-learning libraries beyond PyTorch**
    
    No, you can only use PyTorch and standard libraries we have used in the course.
	You are **not** allowed to use the MONAI library.

2. **Can I use pre-trained models for transfer-learning**
    
    No, your networks must be **trained from scratch** and not utilise any utilities, wrappers or libraries we have not used in the course.

3. **Can I re-use code from the course materials?**
    
    Yes, you can use code from the course materials, but you must ensure that you understand the code that you are using.

4. **Can I use AI tools to generate code?**
    
    You may use AI tools to generate helper functions, but the core of your implementation must be written by you.

5. **General advice**

	- You have one day and a half: organise your time well and think about the tasks that you will need to do to complete the assessment before diving in. Then, build
a list of tasks, prioritise it and allocate time to each task in the list, including breaks and time to rest overnight. You can leave your networks training while you
sleep, but be careful not to burn all your compute units!

	- Set up your development environment carefully: do not connect to a GPU and burn credits while you are writing code or doing other tasks that do not require
 serious compute.

	- Checkpoint your models during training to avoid having to retrain from epoch 0 every time you disconnect your running environment.

	- Test your submission early. In particular, make sure that, when you download your notebook from Colab with all the executed cells, these executed cells contain the output that you want to have visible in the final repository. If not, check that you have saved and uploaded the correct notebook.
 

**Happy coding!**