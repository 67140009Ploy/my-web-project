from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction
from .forms import TransactionForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    transactions = Transaction.objects.all().order_by('-date')
    income = sum(t.amount for t in transactions if t.transaction_type == 'income')
    expense = sum(t.amount for t in transactions if t.transaction_type == 'expense')
    balance = income - expense

    return render(request, 'index.html', {
        'transactions': transactions,
        'income': income,
        'expense': expense,
        'balance': balance
    })
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TransactionForm()
    return render(request, 'add_transaction.html', {'form': form})

def edit_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'add_transaction.html', {'form': form})

def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    transaction.delete()
    return redirect('index')