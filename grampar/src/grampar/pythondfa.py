#!/usr/bin/python
"""
This module performs all basic DFA operations, without pyfst
"""
import sys
from typing import List, Tuple
from operator import attrgetter
from itertools import product
import copy
from .alphabet import createalphabet
from collections import defaultdict
EPSILON = 0xffff

from loguru import logger

logger.remove()

def TropicalWeight(param):
    """
    Returns the emulated fst TropicalWeight
    Args:
        param (str): The input
    Returns:
        bool: The arc weight
    """
    if param == (float('inf')):
        return False
    else:
        return True


class DFAState:
    """The DFA statess"""

    def __init__(self, sid=None):
        """
        Initialization function
        Args:
            sid (int): The state identifier
        Returns:
            None
        """
        self.final = False
        self.initial = False
        self.lookup = False
        self.stateid = sid
        self.arcs = []

    def __iter__(self):
        """Iterator"""
        return iter(self.arcs)



class DFAArc:
    """The DFA transition"""

    def __init__(self, srcstate_id: int, nextstate_id: int, ilabel: int=None):
        """
        The initialization function
        Args:
            srcstate_id (int): The source state identifier
            nextstate_id (int): The destination state identifier
            ilabel (int): The ilabel of symbol corresponding to character 
                          for the transition
        """
        self.srcstate = srcstate_id
        self.nextstate = nextstate_id
        self.ilabel = ilabel

    def __str__(self) -> str:
        return f"Arc from {self.srcstate} to {self.nextstate}, {self.ilabel}"


class syms:
    """The DFA accepted symbols"""

    def __init__(self):
        """Initialize symbols"""
        self.symbols = {}
        self.reversesymbols = {}

    def __getitem__(self, char):
        """
        Finds a symbol identifier based on the input character
        Args:
            char (str): The symbol character
        Returns:
            int: The retrieved symbol identifier
        """
        return self.reversesymbols[char]

    def __setitem__(self, char, num):
        """
        Sets a symbol
        Args:
            char (str): The symbol character
            num (int): The  symbol identifier
        Returns:
           None
        """
        self.symbols[num] = char
        self.reversesymbols[char] = num

    def find(self, num):
        """
        Finds a symbol based on its identifier
        Args:
            num (int): The symbol identifier
        Returns:
            str: The retrieved symbol
        """
        return self.symbols[num]

    def items(self):
        """Returns all stored symbols
        Args:
            None
        Returns:
            dict:The included symbols
        """
        return self.symbols


class PythonDFA(object):
    """A DFA implementation that uses the
    same interface with python symautomata"""
    def __init__(self, alphabet=createalphabet(), skip_alphabets=[]):
        """
        Args:
            alphabet (list): The imput alphabet
        Returns:
            None
        """
        self.states = {}
        self.alphabet = alphabet
        self.skip_alphabets = []
        self.nfa = False
        num = 1
        self.isyms = syms()
        self.osyms = syms()
        for char in alphabet + [EPSILON]:
            self.isyms.__setitem__(char, num)
            self.osyms.__setitem__(char, num)
            num = num + 1
        self.yy_last_accepting_state = None
        self.yy_accept = []
 
    def __str__(self):
        """Describes DFA object"""
        return f"This is a python DFA object with {len(self.states)} states"

    def __getitem__(self, state):
        """
        Retrieves a state
        Args:
            state (int): State identifier
        Returns:
            DFA state: The selected dfa state
        """
        return self.states[state]

    def __setitem__(self, state, newstate=None):
        """
        Sets a new state
        Args:
            state (int): State identifier
            newstate (DFA State): The selected dfa state
        Returns:
            None
        """
        self.states[state] = newstate

    def define(self):
        """If DFA is empty, create a sink state"""
        if len(self.states) == 0:
            for char in self.alphabet:
                self.add_arc(0, 0, char)
                self[0].final = False

    def add_state(self):
        """Adds a new state"""
        sid = len(self.states)
        self.states[sid] = DFAState(sid)
        while len(self.yy_accept) <= sid:
            # Extend the yy_accept list to accommodate the new state
            # This is used to track accepting states
            self.yy_accept.append(0)
        return sid

    def add_arc(self, src, dst, char, no_arc=False):
        """Adds a new Arc
        Args:
            src (int): The source state identifier
            dst (int): The destination state identifier
            char (str): The character for the transition
        Returns:
            None
        """
        # assert type(src) == type(int()) and type(dst) == type(int()), \
        #     "State type should be integer."
        # assert char in self.I
        #
        #print(self.states)
        #print(src)
        for s_idx in [src, dst]:
            if s_idx >= len(self.states):
                for i in range(len(self.states), s_idx + 1):
                    self.states[i] = DFAState(i)
        if no_arc:
            return
        for arc in self.states[src].arcs:
            if arc.ilabel == self.isyms.__getitem__(char) or char == EPSILON:
                self.nfa = True
                break
        self.states[src].arcs.append(
            DFAArc(src, dst, self.isyms.__getitem__(char)))

    def fixminimized(self, alphabet):
        """
        After pyfst minimization,
        all unused arcs are removed,
        and all sink states are removed.
        However this may break compatibility.
        Args:
            alphabet (list): The input alphabet
        Returns:
            None
        """
        return
        # endstate = self.add_state()
        # for state in self.states:
        #     for char in alphabet:
        #         found = 0
        #         for arc in state.arcs:
        #             if self.isyms.find(arc.ilabel) == char:
        #                 found = 1
        #                 break
        #         if found == 0:
        #             self.add_arc(state.stateid, endstate, char)
        #
        # self[endstate].final = False
        #
        # for char in alphabet:
        #     self.add_arc(endstate, endstate, char)

    def _addsink(self, alphabet):
        """
        Adds a sink state
        Args:
            alphabet (list): The input alphabet
        Returns:
            None
        """
        endstate = len(list(self.states))
        for state in self.states.values():
            for char in alphabet:
                found = 0
                for arc in state.arcs:
                    if self.isyms.find(arc.ilabel) == char:
                        found = 1
                        break
                if found == 0:
                    self.add_arc(state.stateid, endstate, char)

        self[endstate].final = False

        for char in alphabet:
            self.add_arc(endstate, endstate, char)

    def consume_input(self, inp, verbose=False):
        # NOTE: ME me me
        """
        Return True/False if the machine accepts/reject the input.
        Args:
            inp (str): input string to be consumed
        Returns:
            bool: A true or false value depending on if the DFA
                accepts the provided input
        """
        if verbose:
            logger.add(sys.stderr, level="DEBUG")
        def _get_cur():
            for state in self.states.values():
                if state.initial:
                    return state
        #cur_state = sorted(
        #    self.states,
        #    key=attrgetter('initial'),
        #    reverse=True)[0]
        cur_state = _get_cur()

        cur_arc = None
        while len(inp) > 0:
            found = False
            if self.yy_accept[cur_state.stateid] > 0:
                self.yy_last_accepting_state = cur_state
            for arc in cur_state.arcs:
                if self.isyms.find(arc.ilabel) == inp[0]:
                    cur_state = self[arc.nextstate]
                    inp = inp[1:]
                    found = True
                    break
            if not found:
                logger.debug(f"Transition not found {cur_state.stateid} {repr(inp[0])}")
                if inp[0] in self.skip_alphabets:
                    logger.debug(f" (but in skip_alphabets)")
                    inp = inp[1:]
                    continue
                return False
        if cur_state.stateid and self.yy_last_accepting_state is not None == 0:
            return self.yy_accept[self.yy_last_accepting_state.stateid] == 1
        return cur_state.final


    def trace_partial_input(self, inp)-> Tuple[List, bool]:
        """
        Return a list of (state, char) traversed by the inp
        """
        traversed = []

        def _get_cur():
            for state in self.states.values():
                if state.initial:
                    return state
        #cur_state = sorted(
        #    self.states,
        #    key=attrgetter('initial'),
        #    reverse=True)[0]
        cur_state = _get_cur()

        while len(inp) > 0:
            found = False
            traversed.append((cur_state.stateid, inp[0]))
            if self.yy_accept[cur_state.stateid] > 0:
                self.yy_last_accepting_state = cur_state
            for arc in cur_state.arcs:
                if self.isyms.find(arc.ilabel) == inp[0]:
                    cur_state = self[arc.nextstate]
                    inp = inp[1:]
                    found = True
                    break
            if not found:
                return traversed, False
        return traversed, cur_state.final


    def empty(self):
        """
        Return True if the DFA accepts the empty language.
        """
        # self.minimize()
        return len(list(self.states)) == 0

    def complement(self, alphabet):
        """
        Returns the complement of DFA
        Args:
            alphabet (list): The input alphabet
        Returns:
            None
        """
        # Original code that treat states as list
        #states = sorted(self.states, key=attrgetter('initial'), reverse=True)
        for state in states.values():
            if state.final:
                state.final = False
            else:
                state.final = True

    def init_from_acceptor(self, acceptor):
        """
        Adds a sink state
        Args:
            alphabet (list): The input alphabet
        Returns:
            None
        """
        self.states = copy.deepcopy(acceptor.states)
        self.alphabet = copy.deepcopy(acceptor.alphabet)
        self.osyms = copy.deepcopy(acceptor.osyms)
        self.isyms = copy.deepcopy(acceptor.isyms)

    def save(self, txt_fst_file_name):
        """
        Save the machine in the openFST format in the file denoted by
        txt_fst_file_name.
        Args:
            txt_fst_file_name (str): The output file
        Returns:
            None
        """
        output_filename = open(txt_fst_file_name, 'w+')
        #state_ids = sorted(self.states, key=attrgetter('initial'), reverse=True)
        state_ids = sorted(self.states, reverse=True)
        #for state in states:
        for state_id in state_ids:
            state = self.states[state_id]
            for arc in state.arcs:
                itext = self.isyms.find(arc.ilabel)
                otext = self.osyms.find(arc.ilabel)
                output_filename.write(
                    '{}\t{}\t{}\t{}\n'.format(
                        state.stateid,
                        arc.nextstate,
                        ord(itext),
                        ord(otext)))
            if state.final:
                output_filename.write('{}\n'.format(state.stateid))
        output_filename.close()

    def load(self, txt_fst_file_name):
        """
        Save the transducer in the text file format of OpenFST.
        The format is specified as follows:
            arc format: src dest ilabel olabel [weight]
            final state format: state [weight]
        lines may occur in any order except initial state must be first line
        Args:
            txt_fst_file_name (str): The input file
        Returns:
            None
        """
        with open(txt_fst_file_name, 'r') as input_filename:
            for line in input_filename:
                line = line.strip()
                split_line = line.split()
                if len(split_line) == 1:
                    self[int(split_line[0])].final = True
                else:
                    self.add_arc(int(split_line[0]), int(split_line[1]),
                                 chr(int(split_line[2])))
                                 #chr(split_line[2]).decode('hex'))


    def minimize(self):
        """Minimizes the DFA using Hopcroft algorithm"""
        self.hopcroft()

    def intersect(self, other):
        """Constructs an unminimized DFA recognizing
        the intersection of the languages of two given DFAs.
        Args:
            other (DFA): The other DFA that will be used
                         for the intersect operation
        Returns:
        Returns:
            DFA: The resulting DFA
        """
        operation = bool.__and__
        self.cross_product(other, operation)
        return  self

    def __and__(self, other):
        """Constructs an unminimized DFA recognizing
               the intersection of the languages of two given DFAs.
               Args:
                   other (DFA): The other DFA that will be used
                                for the intersect operation
               Returns:
                   DFA: The resulting DFA
               """
        self.intersect(other)
        return self

    def symmetric_difference(self, other):
        """Constructs an unminimized DFA recognizing
        the symmetric difference of the languages of two given DFAs.
        Args:
            other (DFA): The other DFA that will be used
                         for the symmetric difference operation
        Returns:
            DFA: The resulting DFA
        """
        operation = bool.__xor__
        self.cross_product(other, operation)
        return  self

    def union(self, other):
        """Constructs an unminimized DFA recognizing the union of the languages of two given DFAs.
        Args:
            other (DFA): The other DFA that will be used
                         for the union operation
        Returns:
            DFA: The resulting DFA
        """
        operation = bool.__or__
        self.cross_product(other, operation)
        return self

    def __or__(self, other):
        """Constructs an unminimized DFA recognizing the union of the languages of two given DFAs.
                Args:
                    other (DFA): The other DFA that will be used
                                 for the union operation
                Returns:
                    DFA: The resulting DFA
                """
        self.union(other)
        return self


    def _epsilon_closure(self, state):
        """
        Returns the epsilon-closure for the state given as input.
        """
        closure = set([state.stateid])
        stack = [state]
        while True:
            if not stack:
                break
            s = stack.pop()
            for arc in s:
                if self.isyms.find(arc.ilabel) != EPSILON or \
                        arc.nextstate in closure:
                    continue
                closure.add(arc.nextstate)
                stack.append(self.states[arc.nextstate])
        return closure


    def determinize(self):
        """
        Transforms a Non Deterministic DFA into a Deterministic
        Args:
            None
        Returns:
            DFA: The resulting DFA

        Creating an equivalent DFA is done using the standard algorithm.
        A nice description can be found in the book:
        Harry R. Lewis and Christos H. Papadimitriou. 1998.
        E
        print target_dfa_statelements of the Theory of Computation.
        """

        # Compute the \epsilon-closure for all states and save it in a diagram
        epsilon_closure = {}
        for state in self.states:
            sid = state.stateid
            epsilon_closure[sid] = self._epsilon_closure(state)

        # Get a transition diagram to speed up computations
        trans_table = {}
        for state in self.states:
            trans_table[state.stateid] = defaultdict(set)
            for arc in state:
                char = self.isyms.find(arc.ilabel)
                trans_table[state.stateid][char].add(arc.nextstate)

        # is_final function:
        # Given a set of nfa states representing a dfa_state return 1 if the
        # corresponding DFA state is a final state, i.e. if any of the
        # corresponding NFA states are final.
        is_final = lambda nfa_states, dfa_state: True \
            if sum([ int(nfa_states[x].final) for x in dfa_state ]) >= 1 \
            else False

        # Precomputation is over, start executing the conversion algorithm
        state_idx = 1
        nfa_states = copy.deepcopy(self.states)
        self.states = []
        # Initialize the new DFA state list
        self.add_state()
        new_initial = epsilon_closure[nfa_states[0].stateid]
        self.states[0].final = is_final(nfa_states, new_initial)

        dfa_state_idx_map = { frozenset(new_initial) : 0 }
        stack = [new_initial]
        while True:
            # Iterate until all added DFA states are processed.
            if not stack:
                break
            # This is a set of states from the NFA
            src_dfa_state = stack.pop()
            src_dfa_state_idx = dfa_state_idx_map[frozenset(src_dfa_state)]
            for char in self.alphabet:
                # Compute the set of target states
                target_dfa_state = set([])
                for nfa_state in src_dfa_state:
                    next_states = \
                        set([y for x in trans_table[nfa_state][char] \
                             for y in epsilon_closure[x] ])
                    target_dfa_state.update(next_states)
                # If the computed state set is not part of our new DFA add it,
                # along with the transition for the current character.
                if frozenset(target_dfa_state) not in dfa_state_idx_map:
                    self.add_state()
                    dfa_state_idx_map[frozenset(target_dfa_state)] = state_idx
                    self.states[state_idx].final = is_final(nfa_states,
                                                            target_dfa_state)
                    state_idx += 1
                    stack.append(target_dfa_state)

                dst_state_idx = dfa_state_idx_map[frozenset(target_dfa_state)]
                self.add_arc(src_dfa_state_idx, dst_state_idx, char)
        return self


    def invert(self):
        """Inverts the DFA final states"""
        for state in self.states:
            if state.final:
                state.final = False
            else:
                state.final = True

    def difference(self, other):
        """Performs the Diff operation between two atomata
        Args:
            other (DFA): The other DFA that will be used
                         for the difference operation
        Returns:
            DFA: The resulting DFA
        """
        other.invert()
        self.intersect(other)
        return self

    def __sub__(self, other):
        """Performs the Diff operation between two atomata
        Args:
            other (DFA): The other DFA that will be used
                        for the difference operation
        Returns:
            DFA: The resulting DFA
        """
        self.difference(other)
        return self


    def hopcroft(self):
        """
        Performs the Hopcroft minimization algorithm
        Args:
            None
        Returns:
            DFA: The minimized input DFA
        """

        def _getset(testset, partition):
            """
            Checks if a set is in a partition
            Args:
                testset (set): The examined set
                partition (list): A list of sets
            Returns:
                bool: A value indicating if it is a member or not
            """
            for part in partition:
                if set(testset) == set(part):
                    return True
            return None

        def _create_transitions_representation(graph):
            """
            In order to speedup the transition iteration using
            the alphabet, the function creates an index
            Args:
                graph (DFA): The input dfa
                state (DFA state): The examined state
            Returns:
                dict: The generated transition map
            """
            return {x.stateid:{self.isyms.find(arc.ilabel): arc.nextstate \
                               for arc in x} for x in graph.states}

        def _create_reverse_transitions_representation(graph):
            """
            In order to speedup the transition iteration using
            the alphabet, the function creates an index
            Args:
                graph (DFA): The input dfa
                state (DFA state): The examined state
            Returns:
                dict: The generated transition map
            """
            return {x.stateid: {self.isyms.find(arc.ilabel): arc.nextstate \
                                for arc in x} for x in graph.states}

        def _reverse_to_source(target, group1):
            """
            Args:
                target (dict): A table containing the reverse transitions for each state
                group1 (list): A group of states
            Return:
                Set: A set of states for which there is a transition with the states of the group
            """
            new_group = []
            for dst in group1:
                new_group += target[dst]
            return set(new_group)

        def _get_group_from_state(groups, sid):
            """
            Args:
                sid (int): The state identifier
            Return:
                int: The group identifier that the state belongs
            """
            for index, selectgroup in enumerate(groups):
                if sid in selectgroup:
                    return index

        def _delta(graph, cur_state, char):
            """
            Function describing the transitions
            Args:
                graph (DFA): The DFA states
                cur_state (DFA state): The DFA current state
                char (str):: The char that will be used for the transition
            Return:
                DFA Node: The next state
            """
            for arc in cur_state.arcs:
                if graph.isyms.find(arc.ilabel) == char:
                    return graph[arc.nextstate]

        def _partition_group(bookeeping, group):
            """
            Args:
                group (list):  A group of states
            Return:
                tuple: A set of two groups
            """
            for (group1, group2) in bookeeping:
                if group & group1 != set() and not group.issubset(group1):
                    new_g1 = group & group1
                    new_g2 = group - group1
                    return (new_g1, new_g2)
                if group & group2 != set() and not group.issubset(group2):
                    new_g1 = group & group2
                    new_g2 = group - group2
                    return (new_g1, new_g2)
            assert False, "Unmatched group partition"

        def _object_set_to_state_list(objectset):
            """
            Args:
                objectset (list): A list of all the DFA states (as objects)
            Return:
                list: A list of all the DFA states (as identifiers)
            """
            return [state.stateid for state in objectset]

        def _get_accepted(graph):
            """
            Find the accepted states
            Args:
                graph (DFA): The DFA states
            Return:
                list: Returns the list of the accepted states
            """
            return [state for state in graph \
                    if  state.final != TropicalWeight(float('inf'))]

        graph = self

        # Find Q
        set_q = set(_object_set_to_state_list(graph.states))
        # We will work with states addresses here instead of states stateid for
        # more convenience
        set_f = set(_object_set_to_state_list(_get_accepted(graph)))
        # Perform P := {F, Q-F}
        set_nf = set_q.copy() - set_f.copy()
        groups = [set_f.copy(), set_nf.copy()]
        bookeeping = [(set_f, set_nf)]

        done = False
        while not done:
            done = True
            new_groups = []
            for selectgroup in groups:
                # _check for each letter if it splits the current group
                for character in self.alphabet:
                    # print('Testing symbol: ', c)
                    target = defaultdict(list)
                    target_states = defaultdict(int)
                    new_g = [set(selectgroup)]
                    for sid in selectgroup:
                        # _check if all transitions using c are going in a state
                        # in the same group. If they are going on a different
                        # group then split
                        deststate = _delta(graph, graph[sid], character)
                        if deststate is None:
                            continue
                        destgroup = _get_group_from_state(groups,
                            deststate.stateid)
                        target[destgroup].append(sid)
                        target_states[destgroup] = deststate.stateid
                    if len(target) > 1:

                        inv_target_states = {
                            v: k for k, v in target_states.iteritems()}
                        new_g = [set(selectedstate) for selectedstate in target.values()]
                        done = False
                        # Get all the partitions of destgroups
                        queue = [set([x for x in target_states.values()])]
                        while queue:
                            top = queue.pop(0)
                            (group1, group2) = _partition_group(bookeeping, top)
                            ng1 = _reverse_to_source(
                                target, [inv_target_states[x] for x in group1])
                            ng2 = _reverse_to_source(
                                target, [inv_target_states[x] for x in group2])

                            bookeeping.append((ng1, ng2))

                            if len(group1) > 1:
                                queue.append(group1)
                            if len(group2) > 1:
                                queue.append(group2)
                        break
                new_groups += new_g

            # End of iteration for the k-equivalence
            # Assign new groups and check if any change occured
            groups = new_groups

        # Make a copy of the old states, and prepare the
        # automaton to host the minimum states

        oldstates = copy.deepcopy(self.states)
        self.states = []
        self.define()

        def findpart(stateid, partitions):
            """Searches for the groupt that the state identifier
            belongs to.
            Args:
                stateid (int): The state identifier
                partitions (list): The list of the groups
            Returns:
                set: The group that the stateid belongs to.
            """
            for group in partitions:
                if stateid in group:
                    return frozenset(group)
            return frozenset(set(            ))

        def add_state_if_not_exists(group, statesmap, final):
            """
            Adds a new state in the final dfa. It initialy checks if
            the group of states is already registered to the automaton.
            If it is registered, the state identifier is returned, or
            else, a new state is added.
            Args:
                group (frozenset):  The group that the state identifier belongs
                statesmap (dict):   A dictionary that maintains the state
                                    identifiers for each forzenset
                final (bool):       A value indicating if the current state is
                                    final
            Returns:
                int: The new state identifier
            """
            if group not in statesmap:
                sid = self.add_state()
                self[sid].final = final
                statesmap[group] = sid
            return statesmap[group]

        statesmap = {}
        self.states = []
        group = findpart(0, groups)
        sid = add_state_if_not_exists(frozenset(list(group)), statesmap,
                                      oldstates[0].final)
        self[sid].initial = True
        for group in groups:
            if len(group) == 0:
                continue
            sid = add_state_if_not_exists(frozenset(group), statesmap,
                                          oldstates[list(group)[0]].final)
            state = next(iter(group))
            for arc in oldstates[state]:
                dst_group = findpart(arc.nextstate, groups)
                dst_sid = add_state_if_not_exists(
                    dst_group, statesmap, oldstates[arc.nextstate].final)
                self.add_arc(sid, dst_sid, graph.isyms.find(arc.ilabel))


    def cross_product(self, dfa_2, accept_method):
        """A generalized cross-product constructor over two DFAs.
        The third argument is a binary boolean function f; a state (q1, q2) in the final
        DFA accepts if f(A[q1],A[q2]), where A indicates the acceptance-value of the state.
        Args:
            dfa_2: The second dfa
            accept_method: The boolean action
        Returns:
            None
        """
        dfa_1states = copy.deepcopy(self.states)
        dfa_2states = dfa_2.states
        self.states = []
        states = {}


        def _create_transitions_representation(graph, state):
            """
            In order to speedup the transition iteration using
            the alphabet, the function creates an index
            Args:
                graph (DFA): The input dfa
                state (DFA state): The examined state
            Returns:
                dict: The generated transition map
            """
            return {self.isyms.find(arc.ilabel): graph[arc.nextstate] for arc in state}


        def _add_state_if_nonexistent(state_a, state_b):
            """
            Adds a new state in the final dfa, which is the
            combination of the input states. The initial and final
            flag is also placed on the new state. If the state already
            exists, its identifier is being returned.
            Args:
                state_a: The fist state identifier
                state_b: The second state identifier
            Returns:
                int: The new state identifier
            """
            if (state_a.stateid, state_b.stateid) not in states:
                states[(state_a.stateid, state_b.stateid)] \
                    = self.add_state()
                self[states[(state_a.stateid, state_b.stateid)]].initial \
                    = state_a.initial and state_b.initial
                self[states[(state_a.stateid, state_b.stateid)]].final \
                    = accept_method(state_a.final, state_b.final)
            return states[(state_a.stateid, state_b.stateid)]

        for state1, state2 in product(dfa_1states, dfa_2states):
            sid1 = _add_state_if_nonexistent(state1, state2)
            transitions_s1 = _create_transitions_representation(dfa_1states, state1)
            transitions_s2 = _create_transitions_representation(dfa_2states, state2)
            for char in self.alphabet:
                sid2 = _add_state_if_nonexistent(
                    transitions_s1[char], transitions_s2[char])
                self.add_arc(sid1, sid2, char)


def get_input_alts(mma: PythonDFA, inp: str, verbose=False):
    """
    Return inp_alt, (True/False) if the machine accepts/reject the input.
    Args:
        - mma (pythondfa.PythonDFA)
        - inp (str): input string to be consumed
    Returns:
        * inp_alt: List of tuples with the following structure:
            (src_state_id, dest_state_id, inp_ilabel, alternatives)
            - mma trans when src_state_id -> dest_state_id @ inp_ilabel
            - each alt in alternatives:
                {next_state_id: [(DFAArc, mutated_input), ...], ...}
                the arcs that transition from src_state_id to next_state_id
        * bool: A true or false value depending on if the DFA 
                accepts the provided input
    """
    def _get_cur():
        for state in mma.states.values():
            if state.initial:
                return state

    full_inp = inp
    cur_state = _get_cur()
    inp_alts = []
    inp_idx = 0
    while len(inp) > 0:
        found = False

        if verbose:
            print("--", cur_state.stateid, inp[0], end=" ")
        prev_state = cur_state
        prev_inp = inp[0]
        prev_inp_ilabel = None

        if mma.yy_accept[cur_state.stateid] > 0:
            mma.yy_last_accepting_state = cur_state
        for arc in cur_state.arcs:
            if mma.isyms.find(arc.ilabel) == inp[0]:
                cur_state = mma[arc.nextstate]
                prev_inp_ilabel = arc.ilabel
                inp = inp[1:]
                found = True
                break
        if not found:
            if inp[0] in mma.skip_alphabets:
                inp = inp[1:]
                continue
            print(" x No transition found")
            return [], False

        if verbose:
            print(cur_state.stateid)

        if inp_idx == 0:
            inp_idx += 1
            continue

        alts = {}
        for alt_arc in prev_state.arcs:
            if alt_arc.nextstate == cur_state.stateid:
                continue
            if alt_arc.nextstate not in alts:
                alts[alt_arc.nextstate] = []
            alt_chr = mma.isyms.find(alt_arc.ilabel) 
            new_inp = full_inp[:inp_idx] + alt_chr + full_inp[inp_idx:]
            if verbose:
                print(f"id: {inp_idx:03d}; arc {alt_arc.srcstate}",
                      "-> {alt_arc.nextstate};",
                      f"new-inp: {repr(alt_chr)} {repr(alt_arc.ilabel)}--", 
                      new_inp)
            alts[alt_arc.nextstate].append((alt_arc, new_inp))

        # Minimize alts [a-f] -> a, [A-F] -> A, [1-9] -> 9
        #               [g-z] -> z, [G-Z] -> Z
        def _alt_replace(mma: PythonDFA,
                         start_sym: str, end_sym: str, sub_sym:str,
                         orig_alts: List[Tuple[DFAArc, str]]
                         )-> List[Tuple[DFAArc, str]]:
            c_range = [chr(c) for c in range(ord(start_sym), ord(end_sym)+1)]
            ilabel_range = [mma.isyms.__getitem__(c) for c in c_range]
            sub_ilabel = mma.isyms.__getitem__(sub_sym)
            orig_ilabels = [arc.ilabel for (arc, _) in orig_alts]
            #print("  -", ilabel_range)
            #print("  -", c_range)
            #print("  +", orig_ilabels)
            #print("  +", [mma.isyms.find(i) for i in orig_ilabels])
            for ilabel in ilabel_range:
                if ilabel not in orig_ilabels:
                    #print(f"{mma.isyms.find(ilabel)} not found")
                    return orig_alts
            new_alts = []
            for (alt_arc, new_inp) in orig_alts:
                if alt_arc.ilabel in ilabel_range:
                    if alt_arc.ilabel != sub_ilabel:
                        continue
                new_alts.append((alt_arc, new_inp))
            #print("++++++++ Replaced!", len(new_alts), len(orig_alts))
            return new_alts

        #print(full_inp[:inp_idx], " xxx ", full_inp[inp_idx:])
        for k in alts.keys():
            for ss, es, subs in [("a", "f", "a"),
                                 ("A", "F", "A"),
                                 ("g", "z", "z"),
                                 ("G", "Z", "Z"),
                                 ("1", "9", "9")
                                 ]:
                alts[k] = _alt_replace(mma, ss, es, subs, alts[k])

        if verbose:
            # print alternative transitions
            print(" - Inp_alt:", prev_state.stateid, cur_state.stateid, prev_inp)
            print("    Alternatives:")
            for k, v in alts.items():
                print("      ", k, [mma.isyms.find(arc.ilabel) for arc,_ in v])
        inp_alts.append((prev_state.stateid, 
                         cur_state.stateid, 
                         prev_inp_ilabel, 
                         alts))
        inp_idx += 1

    if cur_state.stateid and mma.yy_last_accepting_state is not None == 0:
        return inp_alts, mma.yy_accept[mma.yy_last_accepting_state.stateid] == 1
    return inp_alts, cur_state.final
