# encoding:utf-8

from mido import Message, MidiFile, MidiTrack, MetaMessage
import mido
from midi2audio import FluidSynth


mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# 修改乐器音色
track.append(Message('program_change', program=43, time = 0))
# 音符的开始
# track.append(Message('note_on', note=64, velocity=64, time=32))
# 音符的结束
# track.append(Message('note_off', note = 64, velocity = 127, time=32))

# bpm = 125
# tempo = 75
# tempo = mido.bpm2tempo(bpm)
# meta_time = MetaMessage('time_signature', numerator=3, denominator=4)
# meta_tempo = MetaMessage('set_tempo', tempo = tempo, time=0)
# meta_tone = MetaMessage('key_signature', key='C')


'''
meta_time是根据bpm而计算出的每个节拍的时间长度，用于得到Message中的time参数
base_note是通过实验得到的C4的音高，作为根音来搭配major_notes得到每个音符的音高
base_num用于切换目前所在的音域，负值表示低几度，正值表示高几度
velocity是一个0~2的浮点数，以64为基准来进行比较
'''


def play_note(note, length, track, base_num=0, delay=0, velocity=1.0, channel=0):
    bpm = 125
    meta_time = 60 / bpm * 1000 # 一拍多少毫秒，一拍等于一个四分音符
    major_notes = [0, 2, 2, 1, 2, 2, 2, 1]
    base_note = 60 # C4对应的数字
    track.append(Message('note_on', note=base_note + base_num*12 + sum(major_notes[0:note]), velocity=round(64*velocity), time=round(delay*meta_time), channel=channel))
    track.append(Message('note_off', note=base_note + base_num*12 + sum(major_notes[0:note]), velocity=round(64*velocity), time=round(meta_time*length), channel=channel))


'''
def play_note(note, length, track, base_num=0, delay=0, velocity=0, channel=0):
    bpm = 125
    meta_time = 60 / bpm * 1000 # 一拍多少毫秒，一拍等于一个四分音符
    # 每个节拍的时长
    # meta_time = 60*60*10/bpm
    # 音阶结构是“全全半全全全半”
    major_notes = [0, 2, 2, 1, 2, 2, 2, 1]
    # 每个音符的音高
    base_note = 60
    track.append(Message('note_on', note=base_note + base_num*12 + sum(major_notes[0:note]), velocity=round(64*velocity), time=round(delay*meta_time), channel=channel))
    track.append(Message('note_off', note=base_note + base_num*12 + sum(major_notes[0:note]), velocity=round(64*velocity), time=round(meta_time*length), channel=channel))

'''


def xiyouji_verse(track):
    play_note(6, 1.0, track)
    play_note(3, 0.75 ,track, 1)
    play_note(5, 0.25, track, 1)

    play_note(3, 0.5, track, 1)
    play_note(6, 0.5, track)
    play_note(1, 1, track, 1)

    play_note(6, 0.25, track)
    play_note(1, 0.25, track, 1)
    play_note(6, 0.25, track)
    play_note(1, 0.25, track, 1)
    play_note(3, 1, track, 1)

    play_note(3, 0.25, track, 1)
    play_note(2, 0.25, track, 1)
    play_note(3, 0.25, track, 1)
    play_note(1, 0.25, track, 1)
    play_note(6, 1, track)

    play_note(3, 0.75, track, 1)
    play_note(5, 0.25, track, 1)
    play_note(6, 0.5, track, 1)
    play_note(6, 0.5, track, 1)

    play_note(6, 0.5, track, 1)
    play_note(3, 0.5, track, 1)
    play_note(5, 1, track, 1)


    play_note(3, 0.25, track, 1)
    play_note(5, 0.25, track, 1)
    play_note(3, 0.25, track, 1)
    play_note(5, 0.25, track, 1)    
    play_note(6, 0.5, track, 1)
    play_note(6, 0.5, track, 1)

    play_note(6, 0.5, track, 1)
    play_note(3, 0.5, track, 1)
    play_note(5, 1, track, 1)

    play_note(5, 0.5, track, 1)
    play_note(6, 0.5, track, 0)
    play_note(5, 0.5, track, 1)  
    play_note(6, 0.5, track, 0)

    play_note(3, 0.25, track, 1)
    play_note(4, 0.25, track, 1)
    play_note(2, 0.25, track, 1)  
    play_note(3, 0.25, track, 1)
    play_note(1, 1, track, 1)   

    play_note(2, 1, track, 1)
    play_note(2, 1, track, 1)

    play_note(2, 0.5, track, 1)
    play_note(1, 0.25, track, 1)
    play_note(2, 0.25, track, 1)
    play_note(3, 0.5, track, 1)
    play_note(5, 0.5, track, 1)

    play_note(6, 1, track, 1)
    play_note(3, 1, track, 2)
    play_note(3, 1, track, 1)
    play_note(3, 1, track, 2)

    play_note(3, 0.5, track, 1)
    play_note(3, 0.5, track, 2)
    play_note(3, 0.5, track, 1)
    play_note(3, 0.5, track, 2) 

    play_note(3, 0.25, track, 1)
    play_note(4, 0.25, track, 1)
    play_note(2, 0.25, track, 1)  
    play_note(3, 0.25, track, 1)
    play_note(1, 1, track, 1)

    play_note(2, 1, track, 1)
    play_note(2, 1, track, 1)   

    play_note(2, 0.5, track, 1)
    play_note(1, 0.25, track, 1) 
    play_note(2, 0.25, track, 1)
    play_note(3, 0.5, track, 1) 
    play_note(5, 0.5, track, 1) 

    play_note(6, 2, track, 1)


def canon_inD_verse(track):
    # 3-2-1-7-6-5-6-7
    play_note(3, 2, track, 1)
    play_note(2, 2, track, 1)
    play_note(1, 2, track, 1)
    play_note(7, 2, track, 0)
    play_note(6, 2, track, 0)
    play_note(5, 2, track, 0)
    play_note(6, 2, track, 0)
    play_note(7, 2, track, 0)

    # 1-7-6-5-4-3-4-2
    play_note(1, 2, track, 1)
    play_note(7, 2, track, 0)
    play_note(6, 2, track, 0)
    play_note(5, 2, track, 0)
    play_note(4, 2, track, 0)
    play_note(3, 2, track, 0)
    play_note(4, 2, track, 0)
    play_note(2, 2, track, 0)

    play_note(1, 0.5, track, 1)
    play_note(7, 0.5, track, 0)
    play_note(1, 0.5, track, 1)
    play_note(1, 0.5, track, 0)

    play_note(7, 0.5, track, -1)
    play_note(5, 0.5, track, 0)
    play_note(2, 0.5, track, 0)
    play_note(3, 0.5, track, 0)

    play_note(1, 0.5, track, 0)
    play_note(1, 0.5, track, 1)
    play_note(7, 0.5, track, 0)
    play_note(6, 0.5, track, 0)

    play_note(7, 0.5, track, 0)
    play_note(3, 0.5, track, 1)
    play_note(5, 0.5, track, 1)
    play_note(6, 0.5, track, 1)

    play_note(4, 0.5, track, 1)
    play_note(3, 0.5, track, 1)
    play_note(2, 0.5, track, 1)
    play_note(4, 0.5, track, 1)

    play_note(4, 0.5, track, 1)
    play_note(3, 0.5, track, 1)
    play_note(1, 0.5, track, 1)
    play_note(7, 0.5, track, 0)

    play_note(6, 0.5, track, 0)
    play_note(5, 0.5, track, 0)
    play_note(4, 0.5, track, 0)
    play_note(3, 0.5, track, 0)

    play_note(2, 0.5, track, 0)
    play_note(4, 0.5, track, 0)
    play_note(3, 0.5, track, 0)
    play_note(2, 0.5, track, 0)

    play_note(1, 0.5, track, 0)
    play_note(2, 0.5, track, 0)
    play_note(3, 0.5, track, 0)
    play_note(4, 0.5, track, 0)

    play_note(5, 0.5, track, 0)
    play_note(2, 0.5, track, 0)
    play_note(5, 0.5, track, 0)
    play_note(4, 0.5, track, 0)

    play_note(3, 0.5, track, 0)
    play_note(6, 0.5, track, 0)
    play_note(5, 0.5, track, 0)
    play_note(4, 0.5, track, 0)

    play_note(5, 0.5, track, 0)
    play_note(4, 0.5, track, 0)
    play_note(3, 0.5, track, 0)
    play_note(2, 0.5, track, 0)

    play_note(1, 0.5, track, 0)
    play_note(6, 0.5, track, -1)
    play_note(6, 0.5, track, 0)
    play_note(7, 0.5, track, 0)

    play_note(1, 0.5, track, 1)
    play_note(7, 0.5, track, 0)
    play_note(6, 0.5, track, 0)
    play_note(5, 0.5, track, 0)

    play_note(4, 0.5, track, 0)
    play_note(3, 0.5, track, 0)
    play_note(2, 0.5, track, 0)
    play_note(6, 0.5, track, 0)

    play_note(5, 0.5, track, 0)
    play_note(6, 0.5, track, 0)
    play_note(5, 0.5, track, 0)
    play_note(4, 0.5, track, 0)

    play_note(3, 1, track, 0)
    play_note(3, 1, track, 1)
    play_note(2, 2, track, 1)

    play_note(1, 2, track, 1)
    play_note(2, 2, track, 1)

    play_note(1, 1, track, 1)
    play_note(3, 1, track, 1)
    play_note(2, 1, track, 1)
    play_note(4, 1, track, 1)

    play_note(5, 0.5, track, 1)
    play_note(3, 0.25, track, 1)
    play_note(4, 0.25, track, 1)

    play_note(5, 0.5, track, 1)
    play_note(3, 0.25, track, 1)
    play_note(4, 0.25, track, 1)

    play_note(5, 0.25, track, 1)
    play_note(5, 0.25, track, 0)
    play_note(6, 0.25, track, 0)
    play_note(7, 0.25, track, 0)

    play_note(1, 0.25, track, 1)
    play_note(2, 0.25, track, 1)
    play_note(3, 0.25, track, 1)
    play_note(4, 0.25, track, 1)

    play_note(3, 0.5, track, 1)
    play_note(1, 0.25, track, 1)
    play_note(2, 0.25, track, 1)

    play_note(3, 0.5, track, 1)
    play_note(3, 0.25, track, 0)
    play_note(4, 0.25, track, 0)

    play_note(5, 0.25, track, 0)
    play_note(6, 0.25, track, 0)
    play_note(5, 0.25, track, 0)
    play_note(4, 0.25, track, 0)

    play_note(5, 0.25, track, 0)
    play_note(6, 0.25, track, 0)
    play_note(5, 0.25, track, 0)
    play_note(4, 0.25, track, 0)

    play_note(4, 0.5, track, 0)
    play_note(6, 0.25, track, 0)
    play_note(5, 0.25, track, 0)

    play_note(4, 0.5, track, 0)
    play_note(3, 0.25, track, 0)
    play_note(2, 0.25, track, 0)

    play_note(3, 0.25, track, 0)
    play_note(2, 0.25, track, 0)
    play_note(1, 0.25, track, 0)
    play_note(2, 0.25, track, 0)

    play_note(3, 0.25, track, 0)
    play_note(4, 0.25, track, 0)
    play_note(5, 0.25, track, 0)
    play_note(6, 0.25, track, 0)

    play_note(4, 0.5, track, 0)
    play_note(6, 0.25, track, 0)
    play_note(5, 0.25, track, 0)

    play_note(6, 0.5, track, 0)
    play_note(7, 0.25, track, 0)
    play_note(1, 0.25, track, 1)

    play_note(5, 0.25, track, 0)
    play_note(6, 0.25, track, 0)
    play_note(7, 0.25, track, 0)
    play_note(1, 0.25, track, 1)

    play_note(2, 0.25, track, 1)
    play_note(3, 0.25, track, 1)
    play_note(4, 0.25, track, 1)
    play_note(5, 0.25, track, 1)

    play_note(3, 0.5, track, 1)
    play_note(1, 0.25, track, 1)
    play_note(2, 0.25, track, 1)

    play_note(3, 0.5, track, 1)
    play_note(2, 0.25, track, 1)
    play_note(1, 0.25, track, 1)

    play_note(2, 0.25, track, 1)
    play_note(7, 0.25, track, 1)
    play_note(1, 0.25, track, 1)
    play_note(2, 0.25, track, 1)

    play_note(3, 0.25, track, 1)
    play_note(2, 0.25, track, 1)
    play_note(1, 0.25, track, 1)
    play_note(7, 0.25, track, 0)

    play_note(1, 0.5, track, 1)
    play_note(6, 0.25, track, 0)
    play_note(7, 0.25, track, 0)

    play_note(1, 0.5, track, 1)
    play_note(1, 0.25, track, 0)
    play_note(2, 0.25, track, 0)

    play_note(3, 0.25, track, 0)
    play_note(4, 0.25, track, 0)
    play_note(1, 0.25, track, 0)
    play_note(2, 0.25, track, 0)

    play_note(3, 0.25, track, 0)
    play_note(1, 0.25, track, 1)
    play_note(7, 0.25, track, 0)
    play_note(1, 0.25, track, 1)

    play_note(6, 0.5, track, 0)
    play_note(1, 0.25, track, 1)
    play_note(7, 0.25, track, 0)

    play_note(6, 0.5, track, 1)
    play_note(5, 0.25, track, 0)
    play_note(4, 0.25, track, 0)

    play_note(5, 0.25, track, 0)
    play_note(4, 0.25, track, 0)
    play_note(3, 0.25, track, 0)
    play_note(4, 0.25, track, 0)

    play_note(5, 0.25, track, 0)
    play_note(6, 0.25, track, 0)
    play_note(7, 0.25, track, 0)
    play_note(1, 0.25, track, 1)

    play_note(6, 0.5, track, 0)
    play_note(1, 0.25, track, 1)
    play_note(7, 0.25, track, 0)

    play_note(1, 0.5, track, 1)
    play_note(7, 0.25, track, 0)
    play_note(6, 0.25, track, 0)

    play_note(7, 0.25, track, 0)
    play_note(1, 0.25, track, 1)
    play_note(2, 0.25, track, 1)
    play_note(1, 0.25, track, 1)

    play_note(7, 0.25, track, 0)
    play_note(1, 0.25, track, 1)
    play_note(6, 0.25, track, 0)
    play_note(7, 0.25, track, 0)

    play_note(3, 0.5, track, 1)
    play_note(3, 0.5, track, 0)
    play_note(4, 0.5, track, 0)
    play_note(3, 0.5, track, 0)

    play_note(2, 0.5, track, 0)
    play_note(2, 0.5, track, 1)
    play_note(3, 0.5, track, 1)
    play_note(2, 0.5, track, 1)

    play_note(1, 0.5, track, 1)
    play_note(3, 0.5, track, 0)
    play_note(1, 0.5, track, 0)
    play_note(6, 0.5, track, 0)

    play_note(5, 0.5, track, 0)
    play_note(5, 0.5, track, -1)
    play_note(4, 0.5, track, -1)
    play_note(5, 0.5, track, -1)

    play_note(6, 0.5, track, -1)
    play_note(6, 0.5, track, 0)
    play_note(7, 0.5, track, 0)
    play_note(6, 0.5, track, 0)

    play_note(7, 0.5, track, 0)
    play_note(5, 0.5, track, -1)
    play_note(4, 0.5, track, -1)
    play_note(5, 0.5, track, -1)

    play_note(6, 0.5, track, -1)
    play_note(6, 0.5, track, 0)
    play_note(5, 0.5, track, 0)
    play_note(6, 0.5, track, 0)

    play_note(7, 0.5, track, 0)
    play_note(7, 0.5, track, 0)
    play_note(6, 0.5, track, 0)
    play_note(7, 0.5, track, 0)

    play_note(1, 0.5, track, 0)
    play_note(1, 0.5, track, 1)
    play_note(2, 0.5, track, 1)
    play_note(1, 0.5, track, 1)

    play_note(7, 0.5, track, 0)
    play_note(7, 0.5, track, -1)
    play_note(1, 0.5, track, 0)
    play_note(7, 0.5, track, -1)

    play_note(6, 0.5, track, -1)
    play_note(6, 0.5, track, 0)
    play_note(5, 0.5, track, 0)
    play_note(6, 0.5, track, 0)

    play_note(7, 0.5, track, 0)
    play_note(7, 0.5, track, -1)
    play_note(3, 0.5, track, 0)
    play_note(2, 0.5, track, -1)

    play_note(1, 0.5, track, 0)
    play_note(1, 0.5, track, 1)
    play_note(2, 0.5, track, 1)
    play_note(4, 0.5, track, 1)

    play_note(3, 0.5, track, 1)
    play_note(3, 0.5, track, 0)
    play_note(5, 0.5, track, 0)
    play_note(3, 0.5, track, 1)

    play_note(1, 0.5, track, 1)
    play_note(4, 0.5, track, 1)
    play_note(3, 0.5, track, 1)
    play_note(4, 0.5, track, 1)

    play_note(2, 0.5, track, 1)
    play_note(5, 0.5, track, 0)
    play_note(4, 0.5, track, 0)
    play_note(5, 0.5, track, 0)

    play_note(3, 0.5, track, 0)
    play_note(1, 0.25, track, 1)
    play_note(7, 0.25, track, 0)

    play_note(1, 0.5, track, 1)
    play_note(3, 0.5, track, 0)

    play_note(5, 0.5, track, 0)
    play_note(5, 0.25, track, 0)
    play_note(6, 0.25, track, 0)

    play_note(7, 0.5, track, 0)
    play_note(5, 0.5, track, 0)

    play_note(3, 0.5, track, 0)
    play_note(1, 0.25, track, 1)
    play_note(2, 0.25, track, 1)

    play_note(3, 0.5, track, 1)
    play_note(1, 0.5, track, 1)

    play_note(3, 0.5, track, 1)
    play_note(3, 0.25, track, 1)
    play_note(2, 0.25, track, 1)

    play_note(1, 0.5, track, 1)
    play_note(7, 0.5, track, 0)

    play_note(6, 0.5, track, 0)
    play_note(6, 0.25, track, 0)
    play_note(5, 0.25, track, 0)

    play_note(6, 0.5, track, 0)
    play_note(7, 0.5, track, 0)

    play_note(1, 0.5, track, 1)
    play_note(3, 0.25, track, 1)
    play_note(2, 0.25, track, 1)

    play_note(1, 0.5, track, 1)
    play_note(3, 0.5, track, 3)


canon_inD_verse(track)
mid.save('canon_in_D_violin43.mid')

# fs = FluidSynth()
# fs.midi_to_audio('canon_in_D.mid', 'canon_in_D.wav')
