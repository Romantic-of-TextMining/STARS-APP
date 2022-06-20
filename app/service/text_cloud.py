class GenerateTfIdfTag:

    @classmethod
    def transform_tag(self, field_dict):
        for level, token_dict in field_dict.items():
            tagList = []
            minFreq=20000
            for token, tfidf in token_dict.items():
                freq = round(tfidf, 4)*10000 + 1
                if freq < minFreq:
                    minFreq = freq
                tagList.append([token, freq])
            field_dict[level] = {
                "minFreq": minFreq,
                "tagList": tagList
            }
        
        return field_dict
