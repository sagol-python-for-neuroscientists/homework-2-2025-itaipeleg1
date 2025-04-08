from collections import namedtuple
from enum import Enum

Condition = Enum("Condition", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))


def meetup(agent_listing: tuple) -> list:
    """Model the outcome of the meetings of pairs of agents.

    The pairs of agents are ((a[0], a[1]), (a[2], a[3]), ...). If there's an uneven
    number of agents, the last agent will remain the same.

    Notes
    -----
    The rules governing the meetings were described in the question. The outgoing
    listing may change its internal ordering relative to the incoming one.

    Parameters
    ----------
    agent_listing : tuple of Agent
        A listing (tuple in this case) in which each element is of the Agent
        type, containing a 'name' field and a 'category' field, with 'category' being
        of the type Condition.

    Returns
    -------
    updated_listing : list
        A list of Agents with their 'category' field changed according to the result
        of the meeting.
    """
    def worsen(agent: Agent) -> Agent:
        """Worsen the condition of an agent."""
        return Agent(agent.name, Condition(agent.category.value + 1))
    def better(agent: Agent) -> Agent:
        """Cure an agent."""
        return Agent(agent.name, Condition(agent.category.value - 1))
    
    new_listings = []
    
    ## handling the case of healthy and dead agents
    ## we need to remove them from the list and add them to the new list
    indices = []
    for i in range(len(agent_listing)):
         a = agent_listing[i]
         
         if a.category == Condition.DEAD or a.category == Condition.HEALTHY:
             new_listings.append(a)
             indices.append(i)
    agent_listing_new = [a for j, a in enumerate(agent_listing) if j not in indices]
    
    ## handling the case of odd number of agents
    odd = None
    if len(agent_listing_new)%2==1:
        odd = agent_listing_new[-1]


    for i in range(0,len(agent_listing_new),2):
        if i == len(agent_listing_new)-1:
            break
        a1 = agent_listing_new[i]
        a2 = agent_listing_new[i+1]
        conditions = [a1.category, a2.category]

        if a1.category == Condition.CURE:
                new_listings.append(Agent(a1.name, Condition.CURE))
                new_listings.append(better(a2))
        elif a2.category == Condition.CURE:
                new_listings.append(better(a1))
                new_listings.append(Agent(a2.name, Condition.CURE))
                

        elif Condition.SICK in conditions or Condition.DYING in conditions:
            new_listings.append(worsen(a1))
            new_listings.append(worsen(a2))

             
    new_listings.append(odd) if odd else None
    print(new_listings)
    return new_listings

