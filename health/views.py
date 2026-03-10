
from django.shortcuts import render, redirect
from .models import Patient


# ---------------- BASIC PAGES ----------------
def home(request):
    return render(request, 'health/home.html')

def base(request):
    return render(request, 'health/base.html')

def about(request):
    return render(request, 'health/about.html')

def services(request):
    return render(request, 'health/services.html')

def contact(request):
    return render(request, 'health/contact.html')




# ---------------- REGISTER ----------------

def register_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')

        if Patient.objects.filter(email=email).exists():
            return render(request, "health/register.html", {"error": "Email already registered!"})

        # Save user
        user = Patient.objects.create(
            name=name,
            email=email,
            password=password,
            gender=gender
        )

        # ✅ Automatic login after register
        request.session['user_id'] = user.id
        request.session['user_name'] = user.name

        # ✅ Direct doctors page ki redirect
        return redirect("doctors")

    return render(request, "health/register.html")

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Patient.objects.get(email=email, password=password)

            request.session['user_id'] = user.id
            request.session['user_name'] = user.name

            return redirect("doctors")

        except Patient.DoesNotExist:
            return render(request, "health/login.html", {"error": "Invalid Email or Password"})

    return render(request, "health/login.html")

                #-----DOCTORS LIST------#

def doctors_view(request):

    # ✅ Same key check cheyyali
    if not request.session.get("user_id"):
        return redirect("login")

    doctors = [
        {"name": "Dr. Anil Kumar", "spec": "Cardiologist", "exp": 10,
         "hours": "10:00 AM - 2:00 PM", "availability": "Available"},

        {"name": "Dr. Priya Sharma", "spec": "Dermatologist", "exp": 14,
         "hours": "11:00 AM - 4:00 PM", "availability": "On Leave"},

        {"name": "Dr. Ravi Patel", "spec": "Orthopedic", "exp": 8,
         "hours": "9:00 AM - 1:00 PM", "availability": "Available"},

        {"name": "Dr. Neha Verma", "spec": "Gynecologist", "exp": 6,
         "hours": "12:00 PM - 5:00 PM", "availability": "Available"},

        {"name": "Dr. Suresh Reddy", "spec": "Neurologist", "exp": 9,
         "hours": "10:30 AM - 3:30 PM", "availability": "On Leave"},

        {"name": "Dr. Kavita Rao", "spec": "Pediatrician", "exp": 11,
         "hours": "9:30 AM - 1:30 PM", "availability": "Available"},

        {"name": "Dr. Arjun Mehta", "spec": "General Physician", "exp": 13,
         "hours": "8:00 AM - 12:00 PM", "availability": "Available"},

        {"name": "Dr. Pooja Nair", "spec": "ENT Specialist", "exp": 15,
         "hours": "2:00 PM - 6:00 PM", "availability": "Available"},

        {"name": "Dr. Mohan Das", "spec": "Urologist", "exp": 12,
         "hours": "11:00 AM - 3:00 PM", "availability": "On Leave"},

        {"name": "Dr. Ramesh Iyer", "spec": "Oncologist", "exp": 16,
         "hours": "10:00 AM - 4:00 PM", "availability": "Available"},

        {"name": "Dr. Sneha Gupta", "spec": "Psychiatrist", "exp": 7,
         "hours": "1:00 PM - 5:00 PM", "availability": "Available"},

        {"name": "Dr. Vikas Jain", "spec": "Endocrinologist", "exp": 10,
         "hours": "9:00 AM - 2:00 PM", "availability": "Available"},

        {"name": "Dr. Ayesha Khan", "spec": "Pulmonologist", "exp": 9,
         "hours": "12:00 PM - 4:00 PM", "availability": "On Leave"},

        {"name": "Dr. Rohit Malhotra", "spec": "Nephrologist", "exp": 14,
         "hours": "10:00 AM - 1:00 PM", "availability": "Available"},

        {"name": "Dr. Nandini Joshi", "spec": "Rheumatologist", "exp": 8,
         "hours": "11:00 AM - 3:00 PM", "availability": "Available"},
    ]

    return render(request, 'health/doctors.html', {"doctors": doctors})






# ---------------- APPOINTMENT ----------------
def appointment_view(request, doctor, spec):
    if not request.session.get("user_id"):
        return redirect("login")

    if request.method == "POST":
        patient = request.POST.get('patient_name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        time = request.POST.get('time')

        return render(request, 'health/success.html', {
            'patient': patient,
            'doctor': doctor,
            'date': date,
            'time': time
        })

    return render(request, 'health/appointment.html', {
        'doctor_name': doctor,
        'specialization': spec
    })



def logout_view(request):
    request.session.flush()   # 🔥 clears session
    return redirect("login")

