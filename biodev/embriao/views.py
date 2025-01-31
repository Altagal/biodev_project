from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from embriao.models import Botijao, Caneco, Hack, Palheta
from embriao.forms import BotijaoForm, CanecoForm, HackForm, PalhetaForm

#BOTIJAO
@login_required
def botijao_list(request):
    pre_context = {
        "card_title": "Botijao",
    }

    context =  {
        "botijao_list": Botijao.objects.all(),
    }
    return render(request, 'embriao/botijao_list.html', {**pre_context, **context})

@login_required
def botijao_create(request):

    pre_context = {
        "card_title": "Botijao",
    }

    if request.method == 'GET':
        context = {
            "form": BotijaoForm(),
        }

    if request.method == 'POST':
        form = BotijaoForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.custom_save(request)
            return redirect('botijao_list')
        else:
            context = {
                "form": form,
            }

    return render(request, 'embriao/botijao.html', {**pre_context, **context})


@login_required
def botijao_update(request, pk):
    obj = get_object_or_404(Botijao, id=pk)

    pre_context = {
        "card_title": "Botijao",

    }

    if request.method == 'GET':
        context = {
            "form": BotijaoForm(instance=obj),
        }

    if request.method == 'POST':
        form = BotijaoForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.custom_update(request)
            return redirect('botijao_update', obj.id)
        else:
            context = {
                "form": form,
            }

    return render(request, 'embriao/botijao.html', {**pre_context, **context})


@login_required
def botijao_delete(request, pk):
    obj = get_object_or_404(Botijao, id=pk)
    if obj.custom_delete(request):
        return redirect('botijao_list')
    return redirect('botijao_update', obj.id)

#CANECO
def caneco_list(request):
    pre_context = {
        "card_title": "caneco",
    }

    context =  {
        "caneco_list": Caneco.objects.all(),
    }
    return render(request, 'embriao/caneco_list.html', {**pre_context, **context})


@login_required
def caneco_create(request):

    pre_context = {
        "card_title": "Caneco",
    }

    if request.method == 'GET':
        context = {
            "form": CanecoForm(),
        }

    if request.method == 'POST':
        form = CanecoForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.custom_save(request)
            return redirect('caneco_list')
        else:
            context = {
                "form": form,
            }

    return render(request, 'embriao/caneco.html', {**pre_context, **context})


@login_required
def caneco_update(request, pk):
    obj = get_object_or_404(Caneco, id=pk)

    pre_context = {
        "card_title": "Caneco",

    }

    if request.method == 'GET':
        context = {
            "form": CanecoForm(instance=obj),
        }

    if request.method == 'POST':
        form = CanecoForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.custom_update(request)
            return redirect('caneco_list')
        else:
            context = {
                "form": form,
            }

    return render(request, 'embriao/caneco.html', {**pre_context, **context})

@login_required
def caneco_update(request, pk):
    obj = get_object_or_404(Caneco, id=pk)

    pre_context = {
        "card_title": "Caneco",

    }

    if request.method == 'GET':
        context = {
            "form": CanecoForm(instance=obj),
        }

    if request.method == 'POST':
        form = CanecoForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.custom_update(request)
            return redirect('caneco_update', obj.id)
        else:
            context = {
                "form": form,
            }

    return render(request, 'embriao/caneco.html', {**pre_context, **context})


@login_required
def caneco_delete(request, pk):
    obj = get_object_or_404(Caneco, id=pk)
    if obj.custom_delete(request):
        return redirect('caneco_list')
    return redirect('caneco_update', obj.id)

#HACK
def hack_list(request):
    pre_context = {
        "card_title": "hack",
    }

    context =  {
        "hack_list": Hack.objects.all(),
    }
    return render(request, 'embriao/hack_list.html', {**pre_context, **context})


@login_required
def hack_create(request):

    pre_context = {
        "card_title": "Hack",
    }

    if request.method == 'GET':
        context = {
            "form": HackForm(),
        }

    if request.method == 'POST':
        form = HackForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.custom_save(request)
            return redirect('hack_list')
        else:
            context = {
                "form": form,
            }

    return render(request, 'embriao/hack.html', {**pre_context, **context})


@login_required
def hack_update(request, pk):
    obj = get_object_or_404(Hack, id=pk)

    pre_context = {
        "card_title": "Hack",

    }

    if request.method == 'GET':
        context = {
            "form": HackForm(instance=obj),
        }

    if request.method == 'POST':
        form = HackForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.custom_update(request)
            return redirect('hack_list')
        else:
            context = {
                "form": form,
            }

    return render(request, 'embriao/hack.html', {**pre_context, **context})

@login_required
def hack_update(request, pk):
    obj = get_object_or_404(Hack, id=pk)

    pre_context = {
        "card_title": "Hack",

    }

    if request.method == 'GET':
        context = {
            "form": HackForm(instance=obj),
        }

    if request.method == 'POST':
        form = HackForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.custom_update(request)
            return redirect('hack_update', obj.id)
        else:
            context = {
                "form": form,
            }

    return render(request, 'embriao/hack.html', {**pre_context, **context})


@login_required
def hack_delete(request, pk):
    obj = get_object_or_404(Hack, id=pk)
    if obj.custom_delete(request):
        return redirect('hack_list')
    return redirect('hack_update', obj.id)


#PALHETA
def palheta_list(request):
    pre_context = {
        "card_title": "palheta",
    }

    context =  {
        "palheta_list": Palheta.objects.all(),
    }
    return render(request, 'embriao/palheta_list.html', {**pre_context, **context})


@login_required
def palheta_create(request):

    pre_context = {
        "card_title": "Palheta",
    }

    if request.method == 'GET':
        context = {
            "form": PalhetaForm(),
        }

    if request.method == 'POST':
        form = PalhetaForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.custom_save(request)
            return redirect('palheta_list')
        else:
            context = {
                "form": form,
            }

    return render(request, 'embriao/palheta.html', {**pre_context, **context})


@login_required
def palheta_update(request, pk):
    obj = get_object_or_404(Palheta, id=pk)

    pre_context = {
        "card_title": "Palheta",

    }

    if request.method == 'GET':
        context = {
            "form": PalhetaForm(instance=obj),
        }

    if request.method == 'POST':
        form = PalhetaForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.custom_update(request)
            return redirect('palheta_list')
        else:
            context = {
                "form": form,
            }

    return render(request, 'embriao/palheta.html', {**pre_context, **context})

@login_required
def palheta_update(request, pk):
    obj = get_object_or_404(Palheta, id=pk)

    pre_context = {
        "card_title": "Palheta",

    }

    if request.method == 'GET':
        context = {
            "form": PalhetaForm(instance=obj),
        }

    if request.method == 'POST':
        form = PalhetaForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.custom_update(request)
            return redirect('palheta_update', obj.id)
        else:
            context = {
                "form": form,
            }

    return render(request, 'embriao/palheta.html', {**pre_context, **context})


@login_required
def palheta_delete(request, pk):
    obj = get_object_or_404(Palheta, id=pk)
    if obj.custom_delete(request):
        return redirect('palheta_list')
    return redirect('palheta_update', obj.id)