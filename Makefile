source=$(wildcard scratch/all*.step1)
step2=$(source:.step1=.step2)
step3=scratch/step3
step4=scratch/step4
step5=scratch/step5.chk

all: $(step2) $(step3) $(step4) $(step5) 

step1: scratch split.chk 

scratch: 
	@mkdir -p $@

split.chk: 
	split -l 100 -a 4 --additional-suffix=.step1 data/all.txt scratch/all- && \
			touch split.chk

%.step2: %.step1
	python jtnn/mol_tree.py < $< > $@

$(step3): $(step2) 
	cat $^ >> $@

$(step4): $(step3) 
	python bin/unique.py < $< > $@

$(step5): $(step4) 
	mkdir -p scratch/pre_model && \
		CUDA_VISIBLE_DEVICES=0 python molvae/pretrain.py --train data/train.txt --vocab $< \
		--hidden 450 --depth 3 --latent 56 --batch 40 \
		--save_dir scratch/pre_model/ && touch $(step5) 

clean: 
	rm -rf scratch split.chk
