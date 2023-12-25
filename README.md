# CSE534 - Sentiment Analysis using Fabric Testbed


Sentiment Analysis is the process of analysing digital text to determine if the emotional tone of the message is positive, negative, or neutral.

This Sentiment analysis on social media data has become a very valuable tool for businesses which seek rapid feedback from customers. Social media platforms like Twitter (now X) contain an ocean of opinions that can inform decision making if used efficiently. This project examines the integration of real-time sentiment classification with the FABRIC testbed infrastructure to empower business owners through actionable insights from Twitter chatter.

A machine learning model is developed to categorize tweet sentiment as positive (+1), neutral (0), or negative (-1). Custom packets distribute new tweets across the testbed nodes, where sentiment analysis generates useful business intelligence. The first phase establishes a proof of concept on a simple topology. The second phase handles more complex distribution and routing to mimic real-world scenarios. Performance and accuracy are evaluated to validate the approach.

The experiment consists of three setups, to get the results you only need to create and test two of them. The three setups are:
  1. Phase 1
  2. Phase 2
  3. Tradational Method

To setup the Phase 1, you can use the file ACN-Phase1.ipynb by following th steps mentioned in it and the files present in the folder Phase1Files.

To setup the Phase 2, you can use the file ACN-Phase2.ipynb by following the steps mentioned in it and the files present in the folder Phase2Files.

To setup the Tradational method, you can use the file TradationalMethod.ipynb by following the steps mentioned in it and the files present in the folder TradationalMethodFiles.

After successfull execution of Phase2 and Tradational Methods, you can see a map of Id's and timestamp as output on source and destination node. You can use the files GetTimeDifPhase2.ipynb and GetTimeDifTradational.ipynb to get the time it took for the destination to get the sentiment values as output. To get the differences, copy the outputed maps and paste it in place of map1 and map2 for source and destination maps respectively.

Then execute the code and you should be able to get the time diff for each packet sent by the source and also an avergae of all the differences.

On our execution, we got the following results:

For Tradational: Average time difference: 7797.51 milliseconds
For Phase2: Average time difference: 626.62 milliseconds

# CONCLUSION
This project successfully integrates real-time tweet sentiment analysis capabilities within the Fabric testbed. A modular pipeline decomposes the workflow into specialized nodes, improving accuracy and scalability.
Custom packets route encapsulated tweet data through the testbed for processing. Accuracy evaluation shows the model achieves 80-82% precision and recall. Timing metrics meet real-time sub-second latency thresholds.
The solution is proven first on a simple topology, then extended to a complex multi-branch architecture which handles higher throughput with redundancy. 
By leveraging Fabric's capabilities together with custom sentiment analysis components, the project creates a foundation for real-time business intelligence from social media streams. Ongoing work to harden this prototype will help realize benefits like data-driven decision making for business users.

# LIMITATION AND FUTURE WORK

The current approach has limitations in stability and model accuracy at scale. Training on more varied Twitter data could improve generalizability. Exploring algorithms like SVM and CNN could enhance accuracy. Transitioning to standard streaming protocols like Kafka could improve reliability. Encryption of data as it transitions from one node to another is also needed.
Fully hardening performance, precision and robustness across testbed complexity, data volumes and product scenarios would be the next phase of development. More complete failure testing and debugging is also needed. Transitioning the prototype closer to production use cases could realize the potential business benefits

