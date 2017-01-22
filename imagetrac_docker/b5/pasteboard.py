elif "edit" in request.GET:
        form = PostsearchForm() 


        alllinks = []
        worklinks = []
        firstlinks = []
        productlinks = []
        skulinks = []
        imagelinks = []

        show_results = True
        if 'query' in request.GET:
                show_results = True
                query = request.GET['query'].strip()
                if query == "all":
                    alllinks = \
                                Product.objects.all()
                elif query == "work":
                    worklinks = \
                                Product.objects.filter( Q(received_other__iexact='email') | Q(received_other__iexact='ftp'))

                elif query == "fr":
                    firstlinks = \
                                Product.objects.filter(first__iexact='true')

                elif query:
                        form = PostsearchForm({'query' : query})
                        productlinks = \
                                Product.objects.filter( Q(item_no__iexact=query) | Q(item_ns__iexact=query) )
                        skulinks = \
                                Product.objects.filter( Q(sku__iexact=query) | Q(sku_ns__iexact=query) )
                        imagelinks = \
                                ThumbWebfiles.objects.filter(sku__iexact=query)

        # if len(alllinks) >= 1:
        #     user = request.user
        #     records = Product.objects.all()
        #     action = request.POST.get('action')
        #     formset = ProductFormSet(request.POST, queryset=Product.objects.all())

        #     if formset.is_valid():
        #       # iterate over all forms in the formset
        #       for form in formset.forms:
        #         # only do stuff for forms in which is_checked is checked
        #         if form.cleaned_data.get('is_checked'):
        #           if action == u'delete':
        #             # we need to call save to get an actual model but
        #             # there is no need to hit the database hence the
        #             # commit=False
        #             model_instance = form.save(commit=False)
        #             # now that we got a model we can delete it
        #             model_instance.delete()
        #           if action == u'save':
        #             form.save()

        #       redirect('/main')

        #     else:
        #         formset = ProductFormSet(queryset=records)
        #         form = PostsearchForm()
        #         return render_to_response('edit_template.html', {'formset': formset, 'form': form, 'user': user}, context_instance=RequestContext(request))
                

        if len(worklinks) >= 1:
            if request.method == 'POST':
                # we have multiple actions - save and delete in this case
                action = request.POST.get('action')
                formset = ProductFormSet(
                    request.POST, queryset=Product.objects.filter( Q(received_other__iexact='email') | Q(received_other__iexact='ftp')))

                if formset.is_valid():
                  # iterate over all forms in the formset
                    for form in formset.forms:
                    # only do stuff for forms in which is_checked is checked
                        if form.cleaned_data.get('is_checked'):
                            if action == u'delete':
                        # we need to call save to get an actual model but
                        # there is no need to hit the database hence the
                        # commit=False
                                model_instance = form.save(commit=False)
                        # now that we got a model we can delete it
                                model_instance.delete()
                            if action == u'save':
                                form.save()

                    redirect('/main')

            else:
                formset = ProductFormSet(queryset=Product.objects.filter( Q(received_other__iexact='email') | Q(received_other__iexact='ftp')))
                form = PostsearchForm()
            return render_to_response('edit_template.html', {'formset': formset, 'form': form},
                context_instance=RequestContext(request))
                # user = request.user
                # records = Product.objects.filter( Q(received_other__iexact='email') | Q(received_other__iexact='ftp') | Q(first__iexact='t'))
                # action = request.POST.get('action')
                # formset = ProductFormSet(request.POST, queryset=Product.objects.filter( Q(received_other__iexact='email') | Q(received_other__iexact='ftp') | Q(first__iexact='t')))

                # if formset.is_valid():
                #   # iterate over all forms in the formset
                #   for form in formset.forms:
                #     # only do stuff for forms in which is_checked is checked
                #     if form.cleaned_data.get('is_checked'):
                #       if action == u'delete':
                #         # we need to call save to get an actual model but
                #         # there is no need to hit the database hence the
                #         # commit=False
                #         model_instance = form.save(commit=False)
                #         # now that we got a model we can delete it
                #         model_instance.delete()
                #       if action == u'save':
                #         form.save()

                #   redirect('/main')

                # else:
                #     formset = ProductFormSet(queryset=records)
                #     form = PostsearchForm()
                #     return render_to_response('edit_template.html', {'formset': formset, 'form': form, 'user': user}, context_instance=RequestContext(request))
                # if request.method == 'POST':
                #     # we have multiple actions - save and delete in this case
                #     action = request.POST.get('action')
                #     formset = ProductFormSet(
                #       request.POST, queryset=Product.objects.filter( Q(received_other__iexact='email') | Q(received_other__iexact='ftp')))

                #     if formset.is_valid():
                #       # iterate over all forms in the formset
                #         for form in formset.forms:
                #         # only do stuff for forms in which is_checked is checked
                #             if form.cleaned_data.get('is_checked'):

                #                 if action == u'delete':
                #             # we need to call save to get an actual model but
                #             # there is no need to hit the database hence the
                #             # commit=False
                #                     model_instance = form.save(commit=False)
                #             # now that we got a model we can delete it
                #                     model_instance.delete()
                #                 if action == u'save':
                #                     form.save()

                #         redirect('/main')

                # else:
                #     formset = ProductFormSet(queryset=Product.objects.filter( Q(received_other__iexact='email') | Q(received_other__iexact='ftp')))
                #     form = PostsearchForm()

                # return render_to_response('edit_template.html', {'formset': formset, 'form': form},
                #     context_instance=RequestContext(request))
            
                    

        # elif    len(firstlinks) >= 1:
        #         user = request.user
        #         # erecords = Product.objects.filter(received_other__iexact='email')
        #         # ftprecords = Product.objects.filter(received_other__iexact='ftp')
        #         records = Product.objects.filter(first__iexact='true')
        #         # records = list(chain(erecords, ftprecords, firstrecords))
        #         action = request.POST.get('action')
        #         formset = ProductFormSet(request.POST, Product.objects.filter(first__iexact='true'))

        #         if formset.is_valid():
        #           # iterate over all forms in the formset
        #           for form in formset.forms:
        #             # only do stuff for forms in which is_checked is checked
        #             if form.cleaned_data.get('is_checked'):
        #               if action == u'delete':
        #                 # we need to call save to get an actual model but
        #                 # there is no need to hit the database hence the
        #                 # commit=False
        #                 model_instance = form.save(commit=False)
        #                 # now that we got a model we can delete it
        #                 model_instance.delete()
        #               if action == u'save':
        #                 form.save()

        #           redirect('/main')

        #         else:
        #             formset = ProductFormSet(queryset=Product.objects.all())
        #             form = PostsearchForm()
        #             return render_to_response('edit_template.html', {'formset': formset, 'form': form, 'user': user}, context_instance=RequestContext(request))
                     
    else:
        user = request.user
        tpl = "list_template.html"
        form = PostsearchForm()
        variables = RequestContext(request, {'user': user, 'form': form }) 
        return render_to_response(tpl, variables)          
