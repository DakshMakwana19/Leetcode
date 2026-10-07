/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeNodes(ListNode* head) {
        int sum=0;
        ListNode* current=head->next;
        ListNode* write=head;
        while(current!=NULL){
            if(current->val==0){
                write=write->next;
                write->val=sum;
                sum=0;    
            }
            else{
               sum+=current->val; 
            }
            current=current->next;
        }
        write->next=NULL;
        return head->next;
    }
};