#include<types.h>
#include<mmap.h>

/**
 * Function will invoked whenever there is page fault. (Lazy allocation)
 * 
 * For valid acess. Map the physical page 
 * Return 1
 * 
 * For invalid access,
 * Return -1. 
 */
int vm_area_pagefault(struct exec_context *current, u64 addr, int error_code)
{
    int fault_fixed = -1;
    
    return fault_fixed;
}

/**
 * mprotect System call Implementation.
 */
int vm_area_mprotect(struct exec_context *current, u64 addr, int length, int prot)
{
    int isValid = -1;
    return isValid;
}
/**
 * mmap system call implementation.
 */
long vm_area_map(struct exec_context *current, u64 addr, int length, int prot, int flags)
{
    if(length <= 0){
	    return -EINVAL;
    }
    long ret_addr = 0;
    int done = 0;
    int merged = 0;
    int first = 0;
    if(length % PAGE_SIZE != 0){
	    length += (PAGE_SIZE - length % PAGE_SIZE);
    }

    if(addr == NULL){
	//when the address is NOT given
	//In this case we have to find a free space
	struct vm_area * head = current -> vm_area;
	if(head == NULL){
		//In this case we have to create new area starting from the START
		struct vm_area * vm_new = alloc_vm_area();
		current -> vm_area = vm_new;
		vm_new -> vm_start = MMAP_AREA_START;
		vm_new -> vm_end = vm_new -> vm_start + length - 1;
		vm_new -> vm_next = NULL;
		first = 1;
		vm_new -> access_flags = prot;
		done = 1;
		ret_addr = vm_new -> vm_start;
		//We have created new node and set the values now
	}
	else{
		//In this case the head of the linked list is present 
		//that means that some nodes are already present in the vm area
		//so we need to find out space to allocate
		struct vm_area * cur = head;
		struct vm_area * prev = head;
		//cur is an iterator
		while(cur){
			if(cur -> vm_next){
				//we are not in the end now
				int space = cur -> vm_next -> vm_start;
				space -= cur -> vm_end;
				space -= 1;
				//Now space contains the number of memory blocks between
				//those two consecutive vm areas
				if(space >= length){
					//We have found the place
					struct vm_area * vm_new = alloc_vm_area();
					vm_new -> vm_next = cur -> vm_next;
					cur -> vm_next = vm_new;
					vm_new -> vm_start = cur -> vm_end + 1;
					vm_new -> vm_end = vm_new -> vm_start + length - 1;
					vm_new -> access_flags = prot;
					//we have created a new node and inserted it in between
					//the cur and next one
					done = 1;
				        ret_addr = vm_new -> vm_start;	
					break;
				}
				else{
					//This is not the correct place
					prev = cur;
					cur = cur -> vm_next;
					continue;
					//we have to move to the next node
				}
			}
			else{
				//We are at the end of the linked list
				if(cur -> vm_end + length > MMAP_AREA_END){
					//it is not possible to create new area
					//we could not find free space and we have
					//reached the end of the whole area
					return -EINVAL;
				}
				else{
					//We can create a new node at the end
					struct vm_area * vm_new = alloc_vm_area();
					cur -> vm_next = vm_new;
					vm_new -> vm_next = NULL;
					vm_new -> vm_start = cur -> vm_end + 1;
					vm_new -> vm_end = vm_new -> vm_start + length - 1;
					vm_new -> access_flags = prot;
					ret_addr = vm_new -> vm_start;
					done = 1;
					break;
				}
			}
		}
	}
    }
    else{
	//when the address is given
	if(flags & MAP_FIXED){
		//we do not have to use addr as hint address
		int overlap = 0;
		struct vm_area * cur = current -> vm_area;
		struct vm_area * prev = cur;
		if(addr < MMAP_AREA_START || addr + length >= MMAP_AREA_END){
			return -EINVAL;
		}
		if(addr % PAGE_SIZE != 0){
			addr += (PAGE_SIZE - addr % PAGE_SIZE);
			//aligning the address with page size
		}
		if(cur == NULL){
			//we need to make the first element in the linked list
			struct vm_area * vm_new = alloc_vm_area();
			current -> vm_area = vm_new;
			vm_new -> vm_next = NULL;
			vm_new -> vm_start = addr;
			vm_new -> vm_end = addr + length - 1;
			vm_new -> access_flags = prot;
			done = 1;
			first = 1;
			//Here we have created new node and updated the value of vm area head
		}	
		else{
			//Here the linked list has some nodes in it
			//we need to check if the area overlaps with any of already present
			//vm areas for this we will go through the list once
			while(cur){
				if(addr > cur -> vm_end){
					//addr has not arrived yet keeep going
					prev = cur;
					cur = cur -> vm_next;
				}
				else if(addr + length <= cur -> vm_start){
					//before this area we have the address
					//Here we are going to break so we can assume that
					//the first time we are going to arrive here will be 
					//the place where we have to insert
					struct vm_area * vm_new = alloc_vm_area();
					if(prev == cur){
						//In this case the area is before the 
						//first node appears
						vm_new -> vm_next = current -> vm_area;
						current -> vm_area = vm_new;
						vm_new -> vm_start = addr;
						vm_new -> vm_end = addr + length - 1;
						vm_new -> access_flags = prot;
						done = 1;
						first = 1;
					}
					else{
						//Here we have to insert between the cur and 
						//previous node
						prev -> vm_next = vm_new;
						vm_new -> vm_next = cur;
						vm_new -> vm_start = addr;
						vm_new -> vm_end = addr + length - 1;
						vm_new -> access_flags = prot;
						done = 1;
					}
					ret_addr = vm_new;
					break;
				}
				else{
					//In this section there is an overlap
					return -EINVAL;
				}
			}

		}

	}
	else{
		//Here the addr given is hint address
		int overlap = 0;
		struct vm_area * cur = current -> vm_area;
		struct vm_area * prev = cur;
		if(addr < MMAP_AREA_START || addr + length > MMAP_AREA_END){
			//In this case the address is our of range
			overlap = 1;
			//We are setting the value of overlap = 1 as in that case we are going
			//to check for new address and then allocate the memory for the same
		}
		if(cur == NULL){
			//In this case we are going to create a new node
			struct vm_area * vm_new = alloc_vm_area();
	                current -> vm_area = vm_new;
        	        vm_new -> vm_start = addr;
                	vm_new -> vm_end = addr + length - 1;
                	vm_new -> vm_next = NULL;
                	first = 1;
                	vm_new -> access_flags = prot;
                	done = 1;
                	ret_addr = vm_new -> vm_start;
		}
		else{
			//We have a linked list to check
			while(cur && (overlap == 0)){
				//we are going to stop if we reach end or we have found an
				//overlap as in that case we are going to allocate the memory 
				//as if we did not have any address in another for loop
				
				if(cur -> vm_end == addr - 1){
					//Contiguous memory is requested in this case we 
					//are going to merge it into the previous memory
					if(cur -> next){
						//cur has a next element
						if(cur -> vm_next -> vm_start < addr + length){
							//We have an overlap here
							overlap = 1;
							break;
						}
						else{
							//the next memory is not overlapping
							//It is safe to merge the memory now 
							cur -> vm_end = addr + length - 1;
							merged = 1;
							ret_addr = cur -> vm_start;
							done = 1;
							break;
						}
					}
					else{
						//We have a contigous memory after the last 
						//node ..also it is safe to add the last node
						//as the sanity check before the whole block 
						//ensures that the addr + length is not out 
						//of bouds 
						cur -> vm_end = addr + length - 1;
						merged = 1;
						ret_addr = cur;
						done = 1;
						break;
					}
				}
				else if(cur -> vm_start == addr + length){
					//In this case the end of the area is to be merged  
					//also it is clear that the first part of the area is
					//not contiguous with any other area
					//Also the sanity checks ensure that the addr is after
					//the start
					if(prev == cur){
						//We have to merge the first node
						cur -> vm_start = addr;
						merged = 1;
						ret_addr = addr;
						done = 1;
						break;
					}
					else{
						//In this case we have a previous node to 
						//check if it or any node before it -> overlaps
						if(prev -> vm_end >= addr){
							ovberlap = 1;
							break;
						}
						else{
							//we do not have an overlap 
							//it is safe to merge
							cur -> vm_start = addr;
							done = 1;
							merged = 1;
							ret_addr = addr;
							break;
						}
					}
				}
				else if(cur -> vm_end < addr){
					//not arrived yet
					prev = cur;
					cur = cur -> vm_next;
					continue;
				}
				else if(cur -> vm_start >= addr + length){
					//we have gone too far
					break;
				}
				else{
					
				}
				
			}
		}
	}
    }
 
    return ret_addr;
}
/**
 * munmap system call implemenations
 */

int vm_area_unmap(struct exec_context *current, u64 addr, int length)
{
    int isValid = -1;
    return isValid;
}
