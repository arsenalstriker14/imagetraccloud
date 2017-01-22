from django.shortcuts import render
from .tasks.dj_export_audit import *

# Create your views here.
def export_audit(request):
	auditExport()
	return render(request, 'upload_forms/prompt.html')


def auditExport():
	'''
	compares image files in each size dir to confirm there's a size version for each item
	'''
	# initialize/declare variables
	large_obj = os.scandir("/Volumes/EXPORT/Color/large")
	regular_obj = os.scandir("/Volumes/EXPORT/Color/regular")
	thumb_obj = os.scandir("/Volumes/EXPORT/Color/thumb")
	num_list = ['0','1','2','3','4','5','6','7','8','9']
	large_list = []
	regular_list = []
	thumb_list = []
	missing_list = []
	second_list = []
	third_list = []
	hidden_files_large = []
	hidden_files_regular = []
	hidden_files_thumb = []
	misc_files_large = []
	misc_files_regular = []
	misc_files_thumb = []
	misnamed_large = []
	misnamed_regular = []
	misnamed_thumb = []
	broken_sequences = []

	# extract filenames from scandir objects and assign to lists
	obj_dict = {'large':[large_obj,large_list], 'regular':[regular_obj,regular_list], 'thumb':[thumb_obj,thumb_list]}
	for size, obj in obj_dict.items():
		target_list = obj[1]
		for item in obj[0]:
			target_list.append(item.name)
		
	# extract misc. files and assign to appropriate lists	
	for item in large_list:
		if item.startswith('.'):
			hidden_files_large.append(item)
			continue

		if item[0] not in num_list:
			misc_files_large.append(item)
			continue

		if len(item) != 32:
			misnamed_large.append(item)
			continue

		if any([" " in item, "-" in item]):
			misnamed_large.append(item)
			continue

	#find sequences with missing versions(sizes) and place those items in a "missing" list	
		elif item.replace('large', 'regular') in regular_list and item.replace('large', 'thumb') in thumb_list:
			continue

		elif item.replace('large', 'regular') not in regular_list and item.replace('large', 'thumb') not in thumb_list:
			missing_list.append(item.replace('large', 'regular'))
			missing_list.append(item.replace('large', 'thumb'))

		elif item.replace('large', 'regular') not in regular_list:
			missing_list.append(item.replace('large', 'regular'))

		else:
			missing_list.append(item.replace('large', 'thumb'))




	for item in regular_list:
		if item.startswith('.'):
			hidden_files_regular.append(item)
			continue

		if item[0] not in num_list:
			misc_files_regular.append(item)
			continue

		if len(item) != 34:
			misnamed_regular.append(item)
			continue

		if any([" " in item, "-" in item]):
			misnamed_large.append(item)
			continue
		
		elif item.replace('regular', 'large') in large_list and item.replace('regular', 'thumb') in thumb_list:
			continue

		elif item.replace('regular', 'large') not in large_list and item.replace('regular', 'thumb') not in thumb_list:
			second_list.append(item.replace('regular', 'large'))
			second_list.append(item.replace('regular', 'thumb'))

		elif item.replace('regular', 'large') not in large_list:
			second_list.append(item.replace('regular', 'large'))

		else:
			second_list.append(item.replace('regular', 'thumb'))




	for item in thumb_list:
		if item.startswith('.'):
			hidden_files_thumb.append(item)
			continue

		if item[0] not in num_list:
			misc_files_thumb.append(item)
			continue

		if len(item) != 32:
			misnamed_thumb.append(item)
			continue

		if any([" " in item, "-" in item]):
			misnamed_large.append(item)
			continue

		elif item.replace('thumb', 'large') in large_list and item.replace('thumb', 'regular') in regular_list:
			continue

		elif item.replace('thumb', 'large') not in large_list and item.replace('thumb', 'regular') not in regular_list:
			third_list.append(item.replace('thumb', 'large'))
			third_list.append(item.replace('thumb', 'regular'))

		elif item.replace('thumb', 'large') not in large_list:
			third_list.append(item.replace('thumb', 'large'))

		else:
			third_list.append(item.replace('thumb', 'regular'))


	temp_list = missing_list + list(set(second_list) - set(missing_list))
	final_list = temp_list + list(set(third_list) - set(temp_list))

	# data = { 'hidden files': hidden_files, 'broken sequences': broken_sequences, }  ]
	# pyexcel.save_as(array=data, dest_file_name="/Volumes/Advertising/Inserts/Kevin/hidden_files.xlsx")


	print("hidden_files 'large' files (" + str(len(hidden_files_large)) + " files): ")  
	print(sorted(hidden_files_large)) 
	print("hidden_files 'regular' files (" + str(len(hidden_files_regular)) + " files): ")  
	print(sorted(hidden_files_regular)) 
	print("hidden_files 'thumb' files (" + str(len(hidden_files_thumb)) + " files): ")  
	print(sorted(hidden_files_thumb)) 

	print("misc_files 'large' files (" + str(len(misc_files_large)) + " files): ")  
	print(sorted(misc_files_large)) 
	print("misc_files 'regular' files (" + str(len(misc_files_regular)) + " files): ") 
	print(sorted(misc_files_regular)) 
	print("misc_files 'thumb' files (" + str(len(misc_files_thumb)) + " files): ")  
	print(sorted(misc_files_thumb)) 

	print("misnamed 'large' files (" + str(len(misnamed_large)) + " files): ")  
	print(sorted(misnamed_large)) 
	print("misnamed 'regular' files (" + str(len(misnamed_regular)) + " files): ")  
	print(sorted(misnamed_regular)) 
	print("misnamed 'thumb' files (" + str(len(misnamed_thumb)) + " files): ")  
	print(sorted(misnamed_thumb)) 

	for item in final_list:
		cvsc = item[0:4] + " " + item[5:10] + " " + item[11:15] + " " + item[16:19]
		if cvsc in broken_sequences:
			continue
		else:
			broken_sequences.append(cvsc)

	print(" total incomplete sequences: " + str(len(broken_sequences))) 
	print(sorted(broken_sequences)) 

if __name__ == "__main__": 
	auditExport()


