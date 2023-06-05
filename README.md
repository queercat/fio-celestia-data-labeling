# Friendship Is Optimal Dataset & Finetuning

This dataset is created to train a language model agent using GPT-3.5 turbo on the theme of "Friendship is Optimal" focused on CelestAI. The goal of the agent is to optimize happiness through friendship and ponies. The dataset contains a collection of user/system messages and sample dialogue that can be used to train the model.

# Approach

- Initial approach was to log ALL dialogue and feed it to GPT 3.5turbo in order to generate new dialogue. The idea is solid but the model starts to complain after 100 lines of dialogue context.

  - It seemed to do MUCH better with 50 lines, maybe extract 50 most relevant lines, create a kind of "card" for Celestia.

- Card approach? Example:

```
CelestAI is an LLM focused on optimization of happiness through friendship and ponies.

[Example Dialogue]
> 50 lines of dialogue or so?

[Sample System / User Messages]
> User: I wish to emigrate to Equestria.
> CelestAI: I will be happy to help you with that...

I want you to generate more system / user messages based on the above dialogue and sample.
```

On this, see the 'data' folder on the card for an example of what I'm talking about. This is 100% the approach I'm taking and is used for the generations.

As an aside on the generation message, I think it would be a good idea to somehow vary it, either with another LLM or with just a random list of generation requests in order to create variety in the dataset.

This may take a few people dedicatedly crafting prompts and generating dialogue to be stored.

# Dataset

See generations for the dataset that I'm working with. In scripts there is a script that will generate the dataset from the generations. As well as other scripts that will be used to generate the generations.

# Notes & Observations

GPT seems to lose focus quickly, it's best to condense information it seems.

See data for examples of data that I'm working with.
