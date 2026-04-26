import pandas as pd
import matplotlib.pyplot as plt
import os
from django.conf import settings
from django.shortcuts import render, redirect

# ---------------- LOGIN ----------------
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if username:
            return redirect(f'/dashboard/?username={username}')
    return render(request, 'login.html')


# ---------------- DASHBOARD ----------------
def dashboard(request):
    username = request.GET.get('username')

    if not username:
        return redirect('/')

    file_path = os.path.join(settings.BASE_DIR, 'analysis', 'questions.csv')
    df = pd.read_csv(file_path)

    # -------- CLEAN DATA --------
    df['Marks'] = pd.to_numeric(df['Marks'], errors='coerce')
    df['Marks'] = df['Marks'].fillna(0)

    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_cols] = df[numeric_cols].fillna(0)

    text_cols = df.select_dtypes(include=['object']).columns
    df[text_cols] = df[text_cols].fillna("Unknown")

    os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

    # ---------------- GRAPH 1: SUBJECT (COLORED) ----------------
    plt.figure()
    df['Subject'].value_counts().head(5).plot(
        kind='bar',
        color=['red', 'blue', 'green', 'orange', 'purple']
    )
    plt.title("Top Subjects")

    path1 = os.path.join(settings.MEDIA_ROOT, 'graph1.png')
    plt.savefig(path1)
    plt.close()

    subject_table = df['Subject'].value_counts().head(5).to_dict()

    # ---------------- GRAPH 2: DIFFICULTY (DONUT) ----------------
    plt.figure()

    difficulty_counts = df['Difficulty_Level'].value_counts()

    plt.pie(
        difficulty_counts,
        labels=difficulty_counts.index,
        autopct='%1.1f%%'
    )

    # donut effect
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    plt.gca().add_artist(centre_circle)

    plt.title("Difficulty Distribution")

    path2 = os.path.join(settings.MEDIA_ROOT, 'graph2.png')
    plt.savefig(path2)
    plt.close()

    difficulty_table = difficulty_counts.to_dict()

    # ---------------- GRAPH 3: YEAR ----------------
    plt.figure()
    year_counts = df['Year'].value_counts().sort_index()
    year_counts.plot(kind='line')

    plt.title("Year Trend")

    path3 = os.path.join(settings.MEDIA_ROOT, 'graph3.png')
    plt.savefig(path3)
    plt.close()

    year_table = year_counts.tail(5).to_dict()

    # ---------------- GRAPH 4: MARKS PIE ----------------
    plt.figure()

    marks_by_subject = df.groupby('Subject')['Marks'].sum().sort_values(ascending=False).head(5)

    marks_by_subject.plot(kind='pie', autopct='%1.1f%%')

    plt.title("Marks Distribution")

    path4 = os.path.join(settings.MEDIA_ROOT, 'graph4.png')
    plt.savefig(path4)
    plt.close()

    marks_table = marks_by_subject.to_dict()

    return render(request, 'dashboard.html', {
        'username': username,

        'graph1': settings.MEDIA_URL + 'graph1.png',
        'graph2': settings.MEDIA_URL + 'graph2.png',
        'graph3': settings.MEDIA_URL + 'graph3.png',
        'graph4': settings.MEDIA_URL + 'graph4.png',

        'subject_table': subject_table,
        'difficulty_table': difficulty_table,
        'year_table': year_table,
        'marks_table': marks_table,
    })