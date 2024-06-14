class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def get_middle(head):
    '''
    리스트를 중간에서 나누는 함수
    '''
    if head is None:
        return head
    
    slow, fast = head, head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def sorted_merge(left, right):
    '''
    두 정렬된 리스트를 병합하는 함수
    '''
    if left is None:
        return right
    if right is None:
        return left

    if left.value <= right.value:
        result = left
        result.next = sorted_merge(left.next, right)
    else:
        result = right
        result.next = sorted_merge(left, right.next)

    return result

def merge_sort(head):
    '''
    재귀적으로 리스트를 나누고 병합하는 함수
    '''
    if head is None or head.next is None:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    sorted_list = sorted_merge(left, right)
    
    return sorted_list

def print_list(head):
    while head:
        print(head.value, end=" ")
        head = head.next
    print()


if __name__ == "__main__":
    # 링크드 리스트 생성
    head = ListNode(10)
    head.next = ListNode(30)
    head.next.next = ListNode(20)
    head.next.next.next = ListNode(40)
    head.next.next.next.next = ListNode(50)

    print("Given linked list:")
    print_list(head)

    head = merge_sort(head)

    print("Sorted linked list:")
    print_list(head)
