import json





class SearchByTag:

    def __init__(self, data_file, query_tag):
        with open(data_file) as data_file:
            self._data = json.load(data_file)
            #print("here is data ",self._data)
        self.query = query_tag

    def search(self):
        if not self._data or not self.query :
            raise StopIteration
        try:
            self._data['items']
        except KeyError:
            raise StopIteration
        
        for entry in self._data['items']:
            if not entry:
                raise StopIteration
            
            if 'tags' not in entry:
                raise StopIteration
            else:
                for tag in entry['tags']:
                    if tag==self.query:
                        yield entry
            
    def first(self):
        return self.search().__next__()

def main():
    answer=SearchByTag('movies_no_tags.json','crime')
    output=answer.search()
    try:
        for i in output:
            print(i)
    except StopIteration as e:
        print("error")
    
    #print(answer.first())

if __name__=="__main__":
    main()