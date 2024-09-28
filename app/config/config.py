RAW_DATA_PATH = "./dataset/survey_results_public.csv"
DATA_PATH = "./dataset/clean_data.csv"

CKPT_PATH = "./dataset/best_model.joblib"

FEATURE_LIST = ['RemoteWork', 'EdLevel', 'YearsCodePro', 'DevType', 'Country', 'Age',
              'Language', 'Database', 'Platform', 'ToolsTech', 'CollabTool','Salary']

REMOTE_WORK = ['Hybrid', 'Remote', 'Person']

ED_LEVEL = ['Bachelor’s degree', 'Less than a Bachelors', 'Master’s degree','Post grad']

DEV_TYPES =   ['Developer, front-end', 'Developer, full-stack',
              'Developer, back-end', 'System administrator',
              'Developer, QA or test',
              'Data scientist or machine learning specialist',
              'Data or business analyst', 'Security professional',
              'Research & Development role',
              'Developer, embedded applications or devices',
              'Developer, desktop or enterprise applications', 'Engineer, data',
              'Product manager', 'Cloud infrastructure engineer',
              'Senior Executive (C-Suite, VP, etc.)', 'Developer Experience',
              'Engineering manager', 'Developer, mobile', 'DevOps specialist',
              'Engineer, site reliability', 'Project manager',
              'Academic researcher', 'Developer, game or graphics', 'Other']

COUNTRY = ['USA', 'UK', 'Finland', 'Australia', 'Netherlands',
       'Germany', 'Sweden', 'France', 'Spain', 'Brazil', 'Portugal',
       'Italy', 'Canada', 'Switzerland', 'India', 'Austria', 'Norway',
       'Russian Federation', 'Poland', 'Belgium', 'Denmark', 'Israel',
       'Ukraine', 'Czech Republic', 'Romania', 'New Zealand', 'Other']

AGE = ['25-34', '35-44', 'Over 45', '18-24', 'Under 18']

LANGUAGE =    ['HTML/CSS', 'JavaScript', 'Python',
       'Bash/Shell (all shells)', 'SQL', 'TypeScript', 'Java', 'C#',
       'Other language']

DATABASES = ['PostgreSQL', 'Redis', 'MongoDB',
       'Microsoft SQL Server', 'MySQL', 'SQLite', 'Other database']

PLATFORM = ['Amazon Web Services (AWS)', 'Google Cloud', 'Cloudflare', 'Heroku',
       'Firebase', 'Digital Ocean', 'Microsoft Azure', 'Other platform']
TOOLS_TECH = [ 'Docker', 'Kubernetes', 'npm', 'Pip', 'Webpack', 'Yarn', 'Homebrew',
       'Other toolsTech']
       
COLLAB_TOOLS = ['Vim', 'Visual Studio Code', 'IntelliJ IDEA',
       'Android Studio', 'Notepad++', 'Visual Studio', 'Other collabTool']
COLUMNS = ['RemoteWork', 'EdLevel', 'YearsCodePro', 'DevType',
       'Country', 'Age', 'HTML/CSS', 'JavaScript', 'Python',
       'Bash/Shell (all shells)', 'SQL', 'TypeScript', 'Java', 'C#',
       'Other language', 'PostgreSQL', 'Redis', 'MongoDB',
       'Microsoft SQL Server', 'MySQL', 'SQLite', 'Other database',
       'Amazon Web Services (AWS)', 'Google Cloud', 'Cloudflare', 'Heroku',
       'Firebase', 'Digital Ocean', 'Microsoft Azure', 'Other platform',
       'Docker', 'Kubernetes', 'npm', 'Pip', 'Webpack', 'Yarn', 'Homebrew',
       'Other toolsTech', 'Vim', 'Visual Studio Code', 'IntelliJ IDEA',
       'Android Studio', 'Notepad++', 'Visual Studio', 'Other collabTool']
CURRENCY = ['USD','VND', 'EUR','GBP']

CURRENCY_RATES = {'USD': 1.0, 'EUR': 0.9372071227741331, 'GBP': 0.8168228678537958, 'VND' : 24335.00}
CURRENCY_SYMBOLS = {'USD': '$', 'EUR': '€', 'GBP': '£', 'VND' : '₫'}