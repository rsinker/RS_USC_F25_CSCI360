# you can add imports but you should not rely on libraries that are not already provided in "requirements.txt #
from collections import deque
from heapq import heappush, heappop

import numpy as np
import heapq


class TextbookStack(object):
    """A class that tracks the"""

    def __init__(self, initial_order, initial_orientations):
        assert len(initial_order) == len(initial_orientations)
        self.num_books = len(initial_order)

        for i, a in enumerate(initial_orientations):
            assert i in initial_order
            assert a == 1 or a == 0

        self.order = np.array(initial_order)
        self.orientations = np.array(initial_orientations)

    def flip_stack(self, position):
        assert position <= self.num_books

        self.order[:position] = self.order[:position][::-1]
        self.orientations[:position] = np.abs(self.orientations[:position] - 1)[
            ::-1
        ]

    def check_ordered(self):
        for idx, front_matter in enumerate(self.orientations):
            if (idx != self.order[idx]) or (front_matter != 1):
                return False

        return True

    def copy(self):
        return TextbookStack(self.order, self.orientations)

    def __eq__(self, other):
        assert isinstance(
            other, TextbookStack
        ), "equality comparison can only ba made with other __TextbookStacks__"
        return all(self.order == other.order) and all(
            self.orientations == other.orientations
        )

    def __str__(self):
        return f"TextbookStack:\n\torder: {self.order}\n\torientations:{self.orientations}"


def apply_sequence(stack, sequence):
    new_stack = stack.copy()
    for flip in sequence:
        new_stack.flip_stack(flip)
    return new_stack


def a_star_search(stack):
    flip_sequence = []
    pq = []
    counter = 0

    heapq.heappush(pq, (calculate_heuristic(stack, flip_sequence), counter, (stack, flip_sequence)))
    counter += 1

    # --- v ADD YOUR CODE HERE v --- #

    explored_set = set()
    
    while len(pq) != 0:
        priority, tiebreaker, (current_stack, current_sequence) = heapq.heappop(pq)
        stack_key = (tuple(current_stack.order), tuple(current_stack.orientations))
        if stack_key in explored_set:
            continue
        explored_set.add(stack_key)
        
        if current_stack.check_ordered() == True:
            return current_sequence
        
        for flip_position in range(1, current_stack.num_books + 1):
            new_stack = current_stack.copy()
            new_stack.flip_stack(flip_position)
            
            new_sequence = current_sequence + [flip_position]

            heapq.heappush(pq, (calculate_heuristic(new_stack, new_sequence), counter, (new_stack, new_sequence)))
            counter += 1

    return flip_sequence
    # ---------------------------- #

def calculate_heuristic(stack, sequence):
    heuristic = len(sequence)

    for i in range(1, len(stack.order)):
        book1 = stack.order[i - 1]
        book2 = stack.order[i]
    
        book1orientation = stack.orientations[i - 1]
        book2orientation = stack.orientations[i]

        if (abs(book1 - book2) != 1):
            heuristic += 1
            continue
        if (book1orientation != book2orientation):
            heuristic += 1
            continue
        if (book1 > book2 and book1orientation == 1 and book2orientation == 1):
            heuristic += 1
            continue
        if (book1 + 1 == book2 and book1orientation == 0 and book2orientation == 0):
            heuristic += 1
            continue

    return heuristic


def weighted_a_star_search(stack, epsilon=None, N=1):
    # Weighted A* is extra credit

    flip_sequence = []
    # --- v ADD YOUR CODE HERE v --- #

    return flip_sequence

    # ---------------------------- #

if __name__ == "__main__":
    test = TextbookStack(initial_order=[3, 2, 1, 0], initial_orientations=[0, 0, 0, 0])
    output_sequence = a_star_search(test)
    correct_sequence = int(output_sequence == [4])

    new_stack = apply_sequence(test, output_sequence)
    stack_ordered = new_stack.check_ordered()

    print(f"Stack is {'' if stack_ordered else 'not '}ordered")
    print(f"Comparing output to expected traces  - \t{'PASSED' if correct_sequence else 'FAILED'}")